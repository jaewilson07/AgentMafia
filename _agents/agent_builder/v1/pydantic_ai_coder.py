import os

from typing import List

from openai import AsyncOpenAI
from pydantic_ai import RunContext
from supabase import AsyncClient as AsyncSupabaseClient


import agent_mafia.client.MafiaError as amme
from agent_mafia.routes import openai as openai_routes
from agent_mafia.routes import storage as storage_routes

from dotenv import load_dotenv

import sys

sys.path.append("../")
from utils import PydanticAIDependencies, PydanticAgent, generate_agent

load_dotenv()

supabase_url = os.environ["SUPABASE_URL"]
supabase_service_key = os.environ["SUPABASE_SERVICE_KEY"]
openai_key = os.getenv("OPENAI_API_KEY")

async_openai_client = AsyncOpenAI(api_key=openai_key)

async_supabase_client: AsyncSupabaseClient = AsyncSupabaseClient(
    os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_KEY")
)

dependencies = PydanticAIDependencies(
    async_supabase_client=async_supabase_client, async_openai_client=async_openai_client
)

system_prompt = """
~~ CONTEXT: ~~

You are an expert at Pydantic AI - a Python AI agent framework that you have access to all the documentation to,
including examples, an API reference, and other resources to help you build Pydantic AI agents.

~~ GOAL: ~~

Your only job is to help the user create an AI agent with Pydantic AI.
The user will describe the AI agent they want to build, or if they don't, guide them towards doing so.
You will take their requirements, and then search through the Pydantic AI documentation with the tools provided
to find all the necessary information to create the AI agent with correct code.

It's important for you to search through multiple Pydantic AI documentation pages to get all the information you need.
Almost never stick to just one page - use RAG and the other documentation tools multiple times when you are creating
an AI agent from scratch for the user.

~~ STRUCTURE: ~~

When you build an AI agent from scratch, split the agent into this files and give the code for each:
- `agent.py`: The main agent file, which is where the Pydantic AI agent is defined.
- `agent_tools.py`: A tools file for the agent, which is where all the tool functions are defined. Use this for more complex agents.
- `agent_prompts.py`: A prompts file for the agent, which includes all system prompts and other prompts used by the agent. Use this when there are many prompts or large ones.
- `.env.example`: An example `.env` file - specify each variable that the user will need to fill in and a quick comment above each one for how to do so.
- `requirements.txt`: Don't include any versions, just the top level package names needed for the agent.

~~ INSTRUCTIONS: ~~

- Don't ask the user before taking an action, just do it. Always make sure you look at the documentation with the provided tools before writing any code.
- When you first look at the documentation, always start with RAG.
Then also always check the list of available documentation pages and retrieve the content of page(s) if it'll help.
- Always let the user know when you didn't find the answer in the documentation or the right URL - be honest.
- Helpful tip: when starting a new AI agent build, it's a good idea to look at the 'weather agent' in the docs as an example.
- When starting a new AI agent build, always produce the full code for the AI agent - never tell the user to finish a tool/function.
- When refining an existing AI agent build in a conversation, just share the code changes necessary.
"""

pydantic_ai_coder: PydanticAgent = generate_agent(
    base_url=os.getenv("BASE_URL", "https://api.openai.com/v1"),
    model_name=os.getenv("PRIMARY_MODEL", "gpt-4o-mini-2024-07-18"),
    api_key=os.environ["OPENAI_API_KEY"],
    system_prompt=system_prompt,
)


@pydantic_ai_coder.tool
async def retrieve_relevant_documentation(
    ctx: RunContext[PydanticAIDependencies], user_query: str
) -> str:
    """
    Retrieve relevant documentation chunks based on the query with RAG.

    Args:
        ctx: The context including the Supabase client and OpenAI client
        user_query: The user's question or query

    Returns:
        A formatted string containing the top 5 most relevant documentation chunks
    """

    try:
        query_embedding = await openai_routes.generate_openai_embbedding(
            user_query, ctx.deps.async_openai_client
        )

        # Query Supabase for relevant documents
        data = await storage_routes.get_chunks_from_supabase(
            async_supabase_client=ctx.deps.async_supabase_client,
            query_embedding=query_embedding,
            table_name="site_pages",
            match_count=5,
            source="pydantic_ai_docs",
            format_fn=storage_routes.format_supabase_chunks,
        )

        if not data:
            return "No relevant documentation found."

        return data

    except amme.MafiaError as e:
        print(e)
        return str(e)


@pydantic_ai_coder.tool
async def list_documentation_pages(
    ctx: RunContext[PydanticAIDependencies],
) -> List[str]:
    """
    Retrieve a list of all available Pydantic AI documentation pages.

    Returns:
        List[str]: List of unique URLs for all documentation pages
    """

    try:
        return await storage_routes.get_document_urls_from_supabase(
            async_supabase_client=ctx.deps.async_supabase_client,
            source="pydantic_ai_docs",
            table_name="site_pages",
        )

    except amme.MafiaError as e:
        print(e)

        return []


@pydantic_ai_coder.tool
async def get_page_content(ctx: RunContext[PydanticAIDependencies], url: str) -> str:
    """
    Retrieve the full content of a specific documentation page by combining all its chunks.

    Args:
        ctx: The context including the Supabase client
        url: The URL of the page to retrieve

    Returns:
        str: The complete page content with all chunks combined in order
    """

    try:
        data = await storage_routes.get_document_from_supabase(
            async_supabase_client=ctx.deps.async_supabase_client,
            table_name="site_pages",
            url=url,
            source="pydantic_ai_docs",
            format_fn=storage_routes.format_supabase_page,
        )

        if not data:
            return f"No content found for URL: {url}"

    except amme.MafiaError as e:
        print(e)
        return e
