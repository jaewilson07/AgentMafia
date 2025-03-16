import os
from dataclasses import dataclass

from typing import List

from supabase import Client as SupabaseClient
from openai import AsyncClient

from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel

import utils

from src.prompts.agent import pydantic_agent_system_prompt
from src.routes.openai import generate_openai_embbedding

llm = os.getenv("LLM_MODEL", "gpt-4o-mini-2024-07-18")
model = OpenAIModel(llm)


def format_supabase_chunks(data: List[dict]):
    return [
        f"""
# {doc['title']}

{doc['content']}
            """
        for doc in data
    ]


def format_supabase_page(data: List[dict]):
    page_title = data[0]["title"].split(" - ")[0]

    formatted_content = [f"# {page_title}\n"]

    for chunk in data:
        formatted_content.append(chunk["content"])

    return "\n\n".join(formatted_content)


@dataclass
class PydanticAIDependencies:
    supabase: SupabaseClient
    openai_client: AsyncClient


pydantic_ai_expert = Agent(
    model=model,
    system_prompt=pydantic_agent_system_prompt,
    deps_type=PydanticAIDependencies,
    retries=2,
)


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
        message = utils.generate_error_message(e)
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

    except Exception as e:
        message = utils.generate_error_message(
            message="error retrieving documentation pages", exception=e
        )

        print(message)

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

    except Exception as e:
        message = utils.generate_error_message(
            message="error retrieving page content", exception=e
        )
        print(message)

        return message
