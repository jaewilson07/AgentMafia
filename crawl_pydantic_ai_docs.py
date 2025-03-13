from typing import List, Union
import dotenv
import os
import asyncio

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from openai import AsyncOpenAI

dotenv.load_dotenv(override = True)
openai_client = AsyncOpenAI(api_key=os.getenv('OPENAI_KEY'))

def process_and_store_document(url: str, markdown: str):
  """process a document and store chunks in parallel"""

  chunks = chunk_text(markdown)


def crawl_parallel(urls: List[str], max_conccurent_requests: int = 5):
  browser_config = BrowserConfig(
      headless=True,
      verbose=False,
      extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"])


  crawl_config = CrawlerRunConfig(chache_mode = CacheMode.BYPASS)

# create the cralwer instance
crawler = AsyncWebCrawler(config = browser_config)

await crawler.start()

try:
  semaphore = asyncio.Semaphore(max_conccurent_requests)

