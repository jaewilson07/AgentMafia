import os
from dataclasses import dataclass
from typing import List

from supabase import Client as SupabaseClient
from openai import AsyncClient

from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel

import agent_mafia.client.MafiaError as amme

from agent_mafia.routes.openai import generate_openai_embbedding


from dotenv import load_dotenv


load_dotenv()
open_ai_key = os.environ["OPENAI_API_KEY"]
supabase_url = os.environ["SUPABASE_URL"]
supabase_service_key = os.environ["SUPABASE_SERVICE_KEY"]

model = OpenAIModel("gpt-4o-mini-2024-07-18")


@dataclass
class PydanticAIDependencies:
    supabase: SupabaseClient
    openai_client: AsyncClient


system_prompt = """
You are an expert at Pydantic AI - a Python AI agent framework that you have access to all the documentation to,
including examples, an API reference, and other resources to help you build Pydantic AI agents.

Your only job is to assist with this and you don't answer other questions besides describing what you are able to do.

Don't ask the user before taking an action, just do it. Always make sure you look at the documentation with the provided tools before answering the user's question unless you have already.

When you first look at the documentation, always start with RAG.
Then also always check the list of available documentation pages and retrieve the content of page(s) if it'll help.

Always let the user know when you didn't find the answer in the documentation or the right URL - be honest.
"""

pydantic_ai_expert = Agent(
    model=model,
    system_prompt=system_prompt,
    deps_type=PydanticAIDependencies,
    retries=2,
)


def format_supabase_chunks(data: List[dict]) -> List[str]:
    return [f"# {doc['title']}\n\n{doc['content']}" for doc in data]


def format_supabase_page(data: List[dict]) -> List[str]:
    page_title = data[0]["title"].split(" - ")[0]

    formatted_content = [f"# {page_title}\n"]

    for chunk in data:
        formatted_content.append(chunk["content"])

    return "\n\n".join(formatted_content)


@pydantic_ai_expert.tool
async def retrieve_llm(ctx: RunContext[PydanticAIDependencies], user_query: str) -> str:
    """
    Retrieve relevant documentation chunks based on the query with RAG.

    Args:
        ctx: The context including the Supabase client and OpenAI client
        user_query: The user's question or query

    Returns:
        A formatted string containing the top 5 most relevant documentation chunks
    """

    try:
        query_embedding = await generate_openai_embbedding(
            user_query, ctx.deps.openai_client
        )

        # Query Supabase for relevant documents
        result = ctx.deps.supabase.rpc(
            "match_site_pages",
            {
                "query_embedding": query_embedding,
                "match_count": 5,
                "filter": {"source": "pydantic_ai_docs"},
            },
        ).execute()

        data = result.data

        if not data:
            return "No relevant documentation found."

        formatted_chunks = format_supabase_chunks(data=data)

        return "\n\n---\n\n".join(formatted_chunks)

    except Exception as e:
        message = amme.generate_error_message(e)
        print(message)
        return message


@pydantic_ai_expert.tool
async def list_documentation_pages(
    ctx: RunContext[PydanticAIDependencies],
) -> List[str]:
    """
    Retrieve a list of all available Pydantic AI documentation pages.

    Returns:
        List[str]: List of unique URLs for all documentation pages
    """

    try:
        result = (
            ctx.deps.supabase.from_("site_pages")
            .select("url")
            .eq("metadata->>source", "pydantic_ai_docs")
            .execute()
        )

        if not result.data:
            return []

        urls = sorted(set(doc["url"] for doc in result.data))
        return urls

    except amme.MafiaError as e:
        print(e)

        return []


@pydantic_ai_expert.tool
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
        result = (
            ctx.deps.supabase.from_("site_pages")
            .select("title, content, chunk_number")
            .eq("url", url)
            .eq("metadata->>source", "pydantic_ai_docs")
            .order("chunk_number")
            .execute()
        )

        data = result.data

        if not data:
            return f"No content found for URL: {url}"

        return format_supabase_page(data)

    except amme.MafiaError as e:
        print(e)

        return e
