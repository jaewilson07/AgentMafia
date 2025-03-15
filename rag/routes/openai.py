from openai import AsyncOpenAI
from typing import Union, Dict

import json
import os

default_async_openai_client: AsyncOpenAI = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


async def generate_openai_chat(
    messages,
    async_client: AsyncOpenAI = None,
    model: str = "gpt-4o-mini-2024-07-18",
    response_format: Union[Dict[str, str], None] = None,
    return_raw: bool = False,
):

    async_client = async_client or default_async_openai_client

    res = await async_client.chat.completions.create(
        model=model, messages=messages, response_format=response_format
    )

    if return_raw:
        return res

    res = res.choices[0].message.content

    if response_format.get("type") == "json_object":
        res = json.loads(res)

    return res


async def generate_openai_embbedding(
    text,
    async_client: AsyncOpenAI = None,
    model="text-embedding-3-small",
    return_raw: bool = False,
):

    async_client = async_client or default_async_openai_client

    res = await async_client.embeddings.create(model=model, input=text)

    if return_raw:
        return res

    return res.data[0].embedding
