from dotenv import load_dotenv

import os

import asyncio


from supabase import Client as SupabaseClient
from openai import AsyncOpenAI


from agent_mafia.classes.streamlit_ui import streamlit_ui

from pydantic_ai_expert import (
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

title = "Pydantic AI Agenti RAG"
description = "Ask me any question about Pydantic AI"
default_chat_input = "What questions do you have about Pydantic AI?"


async def main():
    await streamlit_ui(
        title=title,
        description=description,
        default_chat_input=default_chat_input,
        agent=agent,
        dependencies=dependencies,
    )


if __name__ == "__main__":
    asyncio.run(main())
