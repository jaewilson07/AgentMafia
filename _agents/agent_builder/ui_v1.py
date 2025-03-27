from agent_mafia.classes.streamlit_ui import streamlit_ui

from dotenv import load_dotenv

import asyncio
import os

from supabase import AsyncClient as AsyncSupabaseClient
from openai import AsyncOpenAI


load_dotenv()

from v1.pydantic_ai_coder import (
    pydantic_ai_coder as v1,
)

import utils

print(v1)

async_openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async_supabase_client: AsyncSupabaseClient = AsyncSupabaseClient(
    os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_KEY")
)

dependencies = utils.PydanticAIDependencies(
    async_supabase_client=async_supabase_client, async_openai_client=async_openai_client
)


async def main():
    await streamlit_ui(
        title="Agent Builder",
        description="Describe an agent and I'll code it for you.",
        default_chat_input="What questions do you have about Pydantic AI?",
        agent=v1,
        dependencies=dependencies,
    )


if __name__ == "__main__":
    asyncio.run(main())
