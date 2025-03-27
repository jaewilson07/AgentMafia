import os


from typing import TypedDict, Annotated, List

from pydantic_ai.messages import ModelMessage, ModelMessagesTypeAdapter

from openai import AsyncOpenAI
from supabase import AsyncClient as AsyncSupabaseClient

from langgraph.config import get_stream_writer
from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt
from langgraph.checkpoint.memory import MemorySaver

from dotenv import load_dotenv

load_dotenv()

import sys
sys.path.append("../")
from .. import utils

from .agents.end_conversation_agent import end_conversation_agent
from .agents.reasoner_agent import reasoner_agent
from .agents.router_agent import router_agent
from .agents.pydantic_ai_coder import pydantic_ai_coder

from agent_mafia.routes import storage as storage_routes


base_url: str = os.getenv("BASE_URL", "https://api.openai.com/v1")
is_ollama = "localhost" in base_url.lower()
api_key: str = os.getenv("LLM_API_KEY", "no-llm-api-key")


async_openai_client: AsyncOpenAI = utils.generate_open_ai_client(base_url, api_key)

async_supabase_client = AsyncSupabaseClient(
    os.environ["SUPABASE_URL"], os.environ["SUPABASE_SERVICE_KEY"]
)


class AgentState(TypedDict):
    """schema of state for the graph"""

    latest_user_message: str
    messages: Annotated[List[bytes], lambda x, y: x + y]
    scope: str


async def define_scope_with_reasoner_node(
    state: AgentState, output_folder="./LOG", scope="pydantic_ai"
):
    # First, get the documentation pages so the reasoner can decide which ones are necessary

    documentation_pages = await storage_routes.get_document_urls_from_supabase(
        async_supabase_client=async_supabase_client,
        source=scope,
        table_name="site_pages",
    )

    documentation_pages_str = "\n".join(documentation_pages)

    # Then, use the reasoner to define the scope
    prompt = f"""
    User AI Agent Request: {state['latest_user_message']}
    
    Create detailed scope document for the AI agent including:
    - Architecture diagram
    - Core components
    - External dependencies
    - Testing strategy

    Also based on these documentation pages available:

    {documentation_pages_str}

    Include a list of documentation pages that are relevant to creating this agent for the user in the scope document.
    """

    result = await reasoner_agent.run(prompt)
    scope = result.data

    # Save the scope to a file
    scope_path = os.path.join(output_folder, "scope.md")

    utils.save_to_markdown(markdown_path=scope_path, data=scope)

    return {"scope": scope}


# Coding Node with Feedback Handling
async def coder_agent_node(state: AgentState, writer, output_folder="./LOG"):
    # Prepare dependencies
    deps = utils.PydanticAIDependencies(
        async_supabase_client=async_supabase_client,
        async_openai_client=async_openai_client,
        reasoner_output=state["scope"],
    )

    # Get the message history into the format for Pydantic AI
    message_history: List[ModelMessage] = []
    for message_row in state["messages"]:
        message_history.extend(ModelMessagesTypeAdapter.validate_json(message_row))

    # Run the agent in a stream
    if is_ollama:
        writer = get_stream_writer()
        result = await pydantic_ai_coder.run(
            state["latest_user_message"], deps=deps, message_history=message_history
        )
        writer(result.data)
    else:
        async with pydantic_ai_coder.run_stream(
            state["latest_user_message"], deps=deps, message_history=message_history
        ) as result:
            # Stream partial text as it arrives
            async for chunk in result.stream_text(delta=True):
                writer(chunk)

    # print(ModelMessagesTypeAdapter.validate_json(result.new_messages_json()))

    coder_path = os.path.join(output_folder, "coder.md")
    utils.save_to_markdown(markdown_path=coder_path, data=result.new_messages_json())

    return {"messages": [result.new_messages_json()]}


def get_next_user_message_node(state: AgentState):
    value = interrupt({})

    # Set the user's latest message for the LLM to continue the conversation
    return {"latest_user_message": value}


async def route_user_message_node(state: AgentState):
    prompt = f"""
    The user has sent a message: 
    
    {state['latest_user_message']}

    If the user wants to end the conversation, respond with just the text "finish_conversation".
    If the user wants to continue coding the AI agent, respond with just the text "coder_agent".
    """

    result = await router_agent.run(prompt)
    next_action = result.data

    if next_action == "finish_conversation":
        return "finish_conversation"
    
    return "coder_agent"


async def end_conversation_node(state: AgentState, writer, output_folder="./LOG"):
    # Get the message history into the format for Pydantic AI
    message_history = [
        ModelMessagesTypeAdapter.validate_json(message_row)
        for message_row in state["messages"]
    ]

    # Run the agent in a stream
    if is_ollama:
        writer = get_stream_writer()
        result = await end_conversation_agent.run(
            state["latest_user_message"], message_history=message_history
        )
        writer(result.data)
    else:
        async with end_conversation_agent.run_stream(
            state["latest_user_message"], message_history=message_history
        ) as result:
            # Stream partial text as it arrives
            async for chunk in result.stream_text(delta=True):
                writer(chunk)

    end_path = os.path.join(output_folder, "end.md")
    utils.save_to_markdown(markdown_path=end_path, data=result.new_messages_json())

    return {"messages": [result.new_messages_json()]}


# Build workflow
builder = StateGraph(AgentState)

builder.add_node("define_scope_with_reasoner", define_scope_with_reasoner_node)
builder.add_node("coder_agent", coder_agent_node)
builder.add_node("get_next_user_message", get_next_user_message_node)
builder.add_node("finish_conversation", end_conversation_node)

# Set edges
builder.add_edge(START, "define_scope_with_reasoner")
builder.add_edge("define_scope_with_reasoner", "coder_agent")
builder.add_edge("coder_agent", "get_next_user_message")
builder.add_conditional_edges(
    "get_next_user_message",
    route_user_message_node,
    {"coder_agent": "coder_agent", "finish_conversation": "finish_conversation"},
)
builder.add_edge("finish_conversation", END)

memory = MemorySaver()

agentic_flow = builder.compile(checkpointer=memory)
