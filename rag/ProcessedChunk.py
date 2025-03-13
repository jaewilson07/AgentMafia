from dataclasses import dataclass

from openai import AsyncOpenAI

from rag import chunk_text as ct
import utils.chunk_execution as ce
from typing import Union, List, Dict
from urllib.parse import urlparse
import datetime as dt
import prompts
import os
import json
from supabase import create_client, Client

default_async_openai_client: AsyncOpenAI = AsyncOpenAI(
    api_key=os.getenv('OPENAI_API_KEY'))

default_supabase_client: Client = create_client(
    os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_KEY"))


async def generate_openai_chat(messages,
                               async_client: AsyncOpenAI = None,
                               model: str = 'gpt-40-mini',
                               response_format: Union[Dict[str, str],
                                                      None] = None,
                               return_raw: bool = False):

  async_client = async_client or default_async_openai_client

  res = await async_client.chat.completions.create(
      model=model, messages=messages, response_format=response_format)

  if return_raw:
    return res

  return res.choices[0].message.content


async def generate_openai_embbedding(
    text,
    async_client: AsyncOpenAI = None,
    model="text-embedding-3-small",
):

  async_client = async_client or default_async_openai_client

  return await async_client.embeddings.create(model=model, input=text)


@dataclass
class ProcessedChunk_Metadata:
  source: str
  crawled_at: str
  url_path: str
  chunk_size: int

  @classmethod
  def _from_url(cls, source, chunk: str, url):
    return cls(source=source,
               crawled_at=dt.datetime.now().isoformat(),
               url_path=urlparse(url).path,
               chunk_size=len(chunk))

  def to_json(self):
    return {
        'source': self.source,
        'crawled_at': self.crawled_at,
        'url_path': self.url_path,
        'chunk_size': self.chunk_size
    }


@dataclass
class ProcessedChunk:
  source: str
  url: str
  chunk_number: int
  title: str
  summary: str
  content: str
  embedding: List[float]
  metadata: Union[ProcessedChunk_Metadata, None] = None
  async_client: Union[AsyncOpenAI, None] = None

  def __post_init__(self):
    if not self.async_client:
      self.async_client = default_async_openai_client

    self.metadata = ProcessedChunk_Metadata._from_url(
        url=self.url,
        source=self.source,
        chunk=self.content,
    )

  @staticmethod
  async def get_title_and_summary(chunk: str,
                                  url: str,
                                  async_client: AsyncOpenAI = None,
                                  model='gpt-40-mini',
                                  return_raw: bool = False) -> dict:

    system_prompt = prompts.prompt_extract_title_and_summary

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": f"URL: {url}\n\nContent:\n{chunk[:1000]}..."
        }  # Send first 1000 chars for context
    ]
    try:
      res = await generate_openai_chat(messages=messages,
                                       async_client=async_client,
                                       model=model,
                                       response_format={"type": "json_object"},
                                       return_raw=return_raw)
      if return_raw:
        return res

      return json.loads(res)

    except Exception as e:
      print(f"Error getting title and summary: {e}")

      return {
          "title": "Error processing title",
          "summary": "Error processing summary"
      }

  @staticmethod
  async def get_embedding(chunk,
                          async_client: AsyncOpenAI = None,
                          model="text-embedding-3-small") -> List[float]:
    try:
      return await generate_openai_embbedding(text=chunk,
                                              async_client=async_client,
                                              model=model)
    except Exception as e:
      print(f"Error creating embedding: {e}")

      return [0] * 1536

  @classmethod
  async def _from_chunk(cls, chunk: str, chunk_number: int, url: str,
                        source: str):

    extracted = await cls.get_title_and_summary(chunk=chunk, url=url)

    embedding = await cls.get_embedding(chunk)

    return cls(
        url=url,
        chunk_number=chunk_number,
        source=source,
        content=chunk,
        summary=extracted['summary'],
        title=extracted['title'],
        embedding=embedding,
    )

  def to_json(self):
    return {
        'url': self.url,
        'chunk_number': self.chunk_number,
        'title': self.title,
        'summary': self.summary,
        'content': self.content,
        'metadata': self.metadata.to_json(),
        'embedding': self.embedding
    }

  async def insert_supabase(
      self,
      supabase_client,
      table_name: str = 'site_pages',  ## see site_pages.sql script
      debug_prn: bool = False):

    try:
      res = await supabase_client.table(table_name).insert(self.to_json()
                                                           ).execute()

      if debug_prn:
        print(
            f"Inserted chunk {self.chunk_number} with id {res.data[0]['id']} for {self.url}"
        )
      return res

    except Exception as e:
      print(f"Error Inserting chunk {self.chunk_number} for {self.url} : {e}")


async def process_and_store_document(url: str,
                                     markdown: str,
                                     source: str,
                                     supabase_client=None,
                                     table_name: str = 'site_pages',
                                     debug_prn: bool = False):
  """process a document and store chunks in parallel"""

  supabase_client = supabase_client or default_supabase_client

  chunks = ct.chunk_text(markdown, debug_prn=debug_prn)

  processed_chunks = await ce.gather_with_concurrency(*[
      ProcessedChunk._from_chunk(chunk=chunk,
                                 chunk_number=i,
                                 url=url,
                                 source=source)
      for i, chunk in enumerate(chunks)
  ],
                                                      n=10)

  return await ce.gather_with_concurrency(*[
      chunk.insert_supabase(supabase_client=supabase_client,
                            table_name=table_name,
                            debug_prn=debug_prn) for chunk in processed_chunks
  ],
                                          n=10)
