import asyncio
from typing import Callable
from crawl4ai import CrawlerRunConfig, CacheMode, BrowserConfig, AsyncWebCrawler
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.deep_crawling.filters import FilterChain, DomainFilter

from agent_mafia.routes.crawler import default_browser_config





async def run_advanced_crawler(
    session_id: str,
    crawler_config: CrawlerRunConfig = None,
    browser_config: BrowserConfig = None,
    storage_fn: Callable = None,
):
    browser_config = browser_config or default_browser_config
    try:

        results = []
        async with AsyncWebCrawler(config=browser_config) as crawler:
            async for res in await crawler.arun(
                "https://api.slack.com",
                config=crawler_config,
                timeout=15,
                session_id=session_id,
            ):
                rgd = ResponseGetDataCrawler.from_res(res)

                if storage_fn:
                    storage_fn(
                        data={
                            "content": res.markdown,
                            "source": session_id,
                            "url": res.url,
                        }
                    )

                results.append(rgd)

        return results

    except NotImplementedError as e:
        raise Crawler_Route_NotSuccess(
            message="have you run create4ai-create and create4ai-doctor? in terminal",
            exception=e,
        )

    except Exception as e:
        raise Crawler_Route_NotSuccess(
            exception=e,
        ) from e

    if not res.success:
        raise Crawler_Route_NotSuccess(
            message=f"error crawling {url} - {res.error_message}"
        )


if __name__ == "__main__":
    asyncio.run(run_advanced_crawler())
