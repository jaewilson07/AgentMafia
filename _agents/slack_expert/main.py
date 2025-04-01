from dotenv import load_dotenv

import os

import asyncio


from supabase import Client as SupabaseClient
from openai import AsyncOpenAI


from agent_mafia.routes.streamlit_ui import streamlit_ui

from _agents.slack_expert.slack_expert import (
    PydanticAIDependencies,
    pydantic_ai_expert as agent,
)


load_dotenv()

openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

supabase: SupabaseClient = SupabaseClient(
    os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_KEY")
)

# logfire.configure(send_to_logfire="never")

dependencies = PydanticAIDependencies(supabase=supabase, openai_client=openai_client)

title = "Slack RAG"
description = "Ask me any question about Slack"
default_chat_input = "What questions do you have about Slack?"


async def main():
    await streamlit_ui(
        title=title,
        description=description,
        default_chat_input=default_chat_input,
    )


if __name__ == "__main__":
    asyncio.run(main())
