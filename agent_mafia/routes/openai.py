"""Default description (change me)"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/routes/openai.ipynb.

# %% auto 0
__all__ = ['default_async_openai_client', 'ChatMessage', 'generate_openai_chat', 'generate_openai_embbedding']

# %% ../../nbs/routes/openai.ipynb 2
from openai import AsyncOpenAI


# %% ../../nbs/routes/openai.ipynb 3
from dataclasses import dataclass
from typing import Union, Dict, List, Literal

import json
import os

from agent_mafia.client.ResponseGetData import ResponseGetDataOpenAi


# %% ../../nbs/routes/openai.ipynb 4
default_async_openai_client: AsyncOpenAI = AsyncOpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)



# %% ../../nbs/routes/openai.ipynb 6
@dataclass
class ChatMessage:
    """Format of messages setn to the browser/API"""

    role: Literal["user", "model"]
    content: str
    timestamp: str = None

    def to_json(self):
        return {
            "role": self.role,
            "content": self.content,
            "timestamp": self.timestamp
        }

async def generate_openai_chat(
    async_client: AsyncOpenAI,
    messages : List[ChatMessage],
    model: str = None, # llm model to use
    response_format: Union[Dict[str, str], None] = None,
    return_raw: bool = False,
):
    clean_message = [ msg.to_json() if isinstance(msg, ChatMessage) else msg for msg in messages]

    res = await async_client.chat.completions.create(
        model=model, messages=clean_message, response_format=response_format
    )

    rgd = ResponseGetDataOpenAi.from_res(res)

    if return_raw:
        return rgd

    content = res.choices[0].message.content
    rgd.response = content

    if response_format and response_format.get("type") == "json_object":
        rgd.response = json.loads(content)

    return rgd

# %% ../../nbs/routes/openai.ipynb 8
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
