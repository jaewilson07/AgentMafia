from openai import AsyncOpenAI
from typing import Union, Dict, List

import json
from dotenv import load_dotenv
import os

load_dotenv()

default_model = os.environ.get("LLM_MODEL", "gpt-4o-mini-2024-07-18")

default_async_openai_client: AsyncOpenAI = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


async def generate_openai_chat(
    messages,
    async_client: AsyncOpenAI = None,
    model: str = None,
    response_format: Union[Dict[str, str], None] = None,
    return_raw: bool = False,
    debug_prn: bool = False,
):
    model = model or default_model
    if debug_prn:
        print("📚 - querying LLM")

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
    debug_prn: bool = False,
) -> List[float]:

    if debug_prn:
        print("📚 - starting LLM")

    async_client = async_client or default_async_openai_client

    res = await async_client.embeddings.create(model=model, input=text)

    if return_raw:
        return res

    return res.data[0].embedding
