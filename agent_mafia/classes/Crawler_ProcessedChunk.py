"""Cralwer uses crawl4ai to download websites as markdown content"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/classes/Crawler.ipynb.

# %% auto 0
__all__ = ['Crawler_ProcessedChunk_Metadata', 'PC_PathNotExist', 'Crawler_ProcessedChunk']

# %% ../../nbs/classes/Crawler.ipynb 2
from dataclasses import dataclass, field
import os
from openai import AsyncOpenAI

import agent_mafia.routes.openai as openai_routes
import agent_mafia.routes.storage as storage_routes
import agent_mafia.prompts.crawler as crawler_prompts

import agent_mafia.client.MafiaError as amme
import agent_mafia.utils.files as amfi

from typing import Union, List
from urllib.parse import urlparse
import datetime as dt

# %% ../../nbs/classes/Crawler.ipynb 3
@dataclass
class Crawler_ProcessedChunk_Metadata:
    source: str
    crawled_at: str
    url_path: str
    chunk_size: int

    @classmethod
    def from_url(cls, source, chunk: str, url):
        return cls(
            source=source,
            crawled_at=dt.datetime.now().isoformat(),
            url_path=urlparse(url).path,
            chunk_size=len(chunk),
        )

    def to_json(self):
        return {
            "source": self.source,
            "crawled_at": self.crawled_at,
            "url_path": self.url_path,
            "chunk_size": self.chunk_size,
        }

# %% ../../nbs/classes/Crawler.ipynb 4
class PC_PathNotExist(amme.MafiaError):
    def __init__(self, md_path):
        super().__init__(f"path {md_path} does not exist")

@dataclass
class Crawler_ProcessedChunk:
    source: str # where a piece of data came from (e.g. a session_id) // could be a complete website or subject area
    url: str
    chunk_number: int
    content: str = field(repr=False) # the actual data 
    title: str = None
    summary: str = None
    embedding: List[float] = None
    metadata: Union[Crawler_ProcessedChunk_Metadata, None] = None
    async_client: Union[AsyncOpenAI, None] = field(repr=False, default=None)
    error_logs: List[str] = field(default_factory=list)

    def __eq__(self, other):
        if self.__class__.__name__ != other.__class__.__name__:
            return False

        return self.url == other.url and self.chunk_number == other.chunk_number

    def __post_init__(self):
        self.metadata = Crawler_ProcessedChunk_Metadata.from_url(
            url=self.url,
            source=self.source,
            chunk=self.content,
        )

    @classmethod
    def from_chunk(
        cls, chunk: str, chunk_number: int, url: str, source: str, output_path=None
    ):

        chunk = cls(
            url=url,
            chunk_number=chunk_number,
            source=source,
            content=chunk,
        )

        if output_path:
            chunk.compare_self_to_disk(output_path)

        return chunk

    @classmethod
    def from_md_file(cls, md_path):
        if not os.path.exists(md_path):
            raise PC_PathNotExist(md_path)

        try:
            chunk, frontmatter = amfi.read_md_from_disk(md_path)

            res = cls(
                url=frontmatter.get("url"),
                source=frontmatter.get("session_id"),
                chunk_number=frontmatter.get("chunk_number"),
                title=frontmatter.get("title"),
                summary=frontmatter.get("summary"),
                embedding=frontmatter.get("embedding"),
                content=chunk,
            )

            return res

        except amme.MafiaError as e:
            print(e)
            return False

    def compare_self_to_disk(self, md_path):
        if not os.path.exists(md_path):
            return False
        
        try:
            md_chunk = self.from_md_file(md_path=md_path)

        except PC_PathNotExist as e:
            print(e)
            return self

        if not md_chunk:
            return self

        if md_chunk.content == self.content:
            self.title = self.title or md_chunk.title
            self.summary = self.summary or md_chunk.summary
            self.embedding = self.embedding or md_chunk.embedding
            self.metadata = md_chunk.metadata
            self.error_logs = md_chunk.error_logs

        return self

    async def get_title_and_summary(
        self,
        is_replace_llm_metadata: bool = False,
        async_client: AsyncOpenAI = None,
        model="gpt-4o-mini-2024-07-18",
        debug_prn: bool = False,
        return_raw: bool = False,
    ) -> dict:

        async_client = async_client or openai_routes.default_async_openai_client

        if not is_replace_llm_metadata and self.title and self.summary:
            if debug_prn:
                print(f"🛢️ {self.url} title and summary already exists")
            return self

        system_prompt = crawler_prompts.prompt_extract_title_and_summary

        messages = [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": f"URL: {self.url}\n\nContent:\n{self.content[:1000]}...",
            },  # Send first 1000 chars for context
        ]
        try:
            res = await openai_routes.generate_openai_chat(
                messages=messages,
                async_client=async_client,
                model=model,
                response_format={"type": "json_object"},
                return_raw=return_raw,
            )

            if return_raw:
                return res

            self.title = res.response.get("title")
            self.summary = res.response.get("summary")

            return res

        except amme.MafiaError as e:
            message = f"Error getting title and summary: {e}"

            print(message)
            self.error_logs.append(message)

            return False

    async def get_embedding(
        self,
        is_replace_llm_metadata: bool = False,
        async_client: AsyncOpenAI = None,
        model="text-embedding-3-small",
        return_raw: bool = False,
        debug_prn: bool = False,
    ) -> List[float]:

        if not is_replace_llm_metadata and self.embedding:

            if debug_prn:
                print(f"🛢️  {self.url} embedding already retrieved")

            return self

        try:
            res = await openai_routes.generate_openai_embedding(
                text=self.content,
                async_client=async_client,
                model=model,
                return_raw=return_raw,
                debug_prn=debug_prn,
            )

            if return_raw:
                return res

            self.embedding = res
            return res

        except amme.MafiaError as e:
            message = f"Error creating embedding: {e}"

            self.error_logs.append(message)

            return False

    async def generate_metadata(
        self,
        is_replace_llm_metadata: bool = False,
        async_text_client: AsyncOpenAI = None,
        async_embedding_model: AsyncOpenAI = None,
        text_model="gpt-4o-mini-2024-07-18",
        embedding_model="text-embedding-3-small",
        debug_prn: bool = False,
        output_path: str = None,
    ):
        await self.get_title_and_summary(
            is_replace_llm_metadata=is_replace_llm_metadata,
            async_client=async_text_client,
            model=text_model,
            debug_prn=debug_prn,
        )
        await self.get_embedding(
            is_replace_llm_metadata=is_replace_llm_metadata,
            async_client=async_embedding_model,
            model=embedding_model,
            debug_prn=debug_prn,
        )

        if output_path:
            storage_routes.save_chunk_to_disk(output_path=output_path,
                                              data = self.to_json())

        return self

    def to_json(self):
        return {
            "url": self.url,
            "source": self.source,
            "chunk_number": self.chunk_number,
            "title": self.title or "No Title",
            "summary": self.summary or "No Summary",
            "content": self.content,
            "metadata": self.metadata.to_json(),
            "embedding": self.embedding or [0] * 1536,
        }
