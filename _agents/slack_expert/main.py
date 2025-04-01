import os
import asyncio

from dotenv import load_dotenv
from openai import AsyncOpenAI
from supabase import Client as SupabaseClient
from pydantic_ai.messages import (
    ModelResponse,
    TextPart,
)

from pydantic_ai.messages import (
    ModelResponse,
    TextPart,
)

from agent_mafia.routes.streamlit_ui import streamlit_ui, st

from _agents.slack_expert.slack_expert import (
    PydanticAIDependencies,
    pydantic_ai_expert as agent,
)

load_dotenv()

openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

supabase: SupabaseClient = SupabaseClient(os.getenv("SUPABASE_URL"),
                                          os.getenv("SUPABASE_SERVICE_KEY"))

# logfire.configure(send_to_logfire="never")

dependencies = PydanticAIDependencies(supabase=supabase,
                                      openai_client=openai_client)

title = "Slack RAG"
description = "Ask me any question about Slack"
default_chat_input = "What questions do you have about Slack?"


async def run_agent_with_streaming(user_input: str, st):
    """
    Run the agent with streaming text for the user_input prompt,
    while maintaining the entire conversation in `st.session_state.messages`.
    """

    async with agent.run_stream(
            user_prompt=user_input,
            deps=dependencies,
            message_history=st.session_state.
            messages[:-1],  # pass entire conversation so far
    ) as result:
        # gather partial text to show streaming results incrementally

        partial_text = ""

        message_placeholder = st.empty()

        # render partial_text as it arrives
        async for chunk in result.stream_text(delta=True):
            partial_text += chunk
            message_placeholder.markdown(partial_text)

        # add new messages excluding initial user_prompt
        filtered_messages = [
            msg for msg in result.new_messages()
            if not (hasattr(msg, "parts") and any(
                part.part_kind == "user-prompt" for part in msg.parts))
        ]
        st.session_state.messages.extend(filtered_messages)

        # Add the final response to the messages
        st.session_state.messages.append(
            ModelResponse(parts=[TextPart(content=partial_text)]))


async def main():
    await streamlit_ui(title=title,
                       description=description,
                       default_chat_input=default_chat_input,
                       run_agent_with_streaming=run_agent_with_streaming)


if __name__ == "__main__":
    asyncio.run(main())
