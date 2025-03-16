from __future__ import annotations
from functools import partial

from dotenv import load_dotenv

from typing import Literal, TypedDict
from enum import Enum
import asyncio
import os

import streamlit as st
import json
import logfire
from supabase import Client as SupabaseClient
from openai import AsyncOpenAI

from pydantic_ai.messages import (
    ModelMessage,
    ModelRequest,
    ModelResponse,
    SystemPromptPart,
    UserPromptPart,
    TextPart,
    ToolCallPart,
    ToolReturnPart,
    RetryPromptPart,
    ModelMessagesTypeAdapter,
)

from src import PydanticAIDependencies, pydantic_ai_expert


load_dotenv()

openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

supabase: SupabaseClient = SupabaseClient(
    os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_KEY")
)

# Configure logfire to suppress warnings (optional)
logfire.configure(send_to_logfire="never")


class ChatMessage(TypedDict):
    """Format of messages setn to the browser/API"""

    role: Literal["user", "model"]
    timestamp: str
    content: str


def display_system_prompt(content):
    with st.chat_message("system"):
        st.markdown(f"**System**: {content}")


def display_user_prompt(content):
    with st.chat_message("user"):
        st.markdown(content)


def display_text(content):
    with st.chat_message("assistant"):
        st.markdown(content)


def display_message_part(part):
    """
    Display a single part of a message in the Streamlit UI.
    Customize how you display system prompts, user prompts,
    tool calls, tool returns, etc.
    """

    class MessagePartEnum(Enum):
        """enum for parsing the correct function to use to display a part_kind"""

        SYSTEM_PROMPT = partial(display_system_prompt)
        USER_PROMPT = partial(display_user_prompt)
        TEXT = partial(display_text)

    MessagePartEnum[part.part_kind.replace("-", "_").upper()].value(
        content=part.content
    )


async def run_agent_with_streaming(user_input: str):
    """
    Run the agent with streaming text for the user_input prompt,
    while maintaining the entire conversation in `st.session_state.messages`.
    """

    dependencies = PydanticAIDependencies(
        supabase=supabase, openai_client=openai_client
    )

    async with pydantic_ai_expert.run_stream(
        user_prompt=user_input,
        deps=dependencies,
        message_history=st.session_state.messages[
            :-1
        ],  # pass entire conversation so far
    ) as result:
        # gather partial text to show streaming results incrementally

        partial_text = ""

        message_placeholder = st.empty()

        # render partial_text as it arrives
        async for chunk in result.stream_text(dela=True):
            partial_text += chunk
            message_placeholder.markdown(partial_text)

        # add new messages excluding initial user_prompt
        filtered_messages = [
            msg
            for msg in result.new_messages()
            if not (hasattr(msg, "parts") and any.part.part_kind == "user-prompt")
        ]

        st.session_state.messages.extend(filtered_messages)

        # add final response to the messages
        st.session_state.messages.append(
            ModelResponse(parts=[TextPart(content=partial_text)])
        )


async def pydantic_streamlit_ui():
    st.title("Pydantic AI Agenti RAG")
    st.write("Ask me any question about Pydantic AI")

    # initialize chat history
    # if "messages" not in st.session_state:
    #     st.session_state.messages = []

    # display all messages so far
    # each message is either a ModelRequest or ModelResponse
    # for msg in st.session_state.messages:
    #     if isinstance(msg, ModelRequest) or isinstance(msg, ModelResponse):
    #         for part in msg.parts:
    #             display_message_part(part)

    user_input = st.chat_input("What questions do you have about Pydantic AI?")

    # if user_input:
    #     st.session_state.messages.append(
    #         ModelRequest(parts=[UserPromptPart(content=user_input)])
    #     )

    # with st.chat_message("assistant"):
    #     await run_agent_with_streaming(user_input)
