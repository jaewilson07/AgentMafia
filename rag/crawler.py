from typing import List
import dotenv
import os

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from openai import AsyncOpenAI

from rag.ProcessedChunk import process_and_store_document
import utils.chunk_execution as ce

dotenv.load_dotenv(override=True)


async def process_url(crawler: AsyncWebCrawler, url: str,
                      crawl_config: CrawlerRunConfig, session_id: str):
  res = await crawler.arun(url=url, config=crawl_config, session_id=session_id)

  if not res.is_success:
    print(f"Error processing url {url} : {res.error_message}")
    return False

  print(f"successfully crawled: {url}")
  return await process_and_store_document(
      url=url,
      markdown=res.markdown_v2.raw_markdown,
      source=session_id,
      debug_prn=True)


async def crawl_parallel(
    urls: List[str | None],
    session_id: str,
    max_conccurent_requests: int = 5,
):
  if not urls:
    print("No URLs found to crawl")
    return

  browser_config = BrowserConfig(
      headless=True,
      verbose=False,
      extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"])

  crawl_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)

  # create the cralwer instance
  crawler = AsyncWebCrawler(config=browser_config)

  await crawler.start()

  try:
    return await ce.gather_with_concurrency(*[
        process_url(url=url,
                    crawler=crawler,
                    crawl_config=crawl_config,
                    session_id=session_id)
    ],
                                            n=max_conccurent_requests)

  except Exception as e:
    print(f"Error crawling urls: {e}")

  finally:
    await crawler.close()
