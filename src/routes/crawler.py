from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

from src.routes import storage

default_browser_config = BrowserConfig(
    browser_type="chromium",
    headless=True,
    verbose=True,
    extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
)


class Crawler_NotSuccess(Exception):
    def __init__(self, url, message):
        super().__init__(f"{url} - {message}")


async def scrape_url(
    url: str,
    session_id: str,
    browser_config: BrowserConfig = None,
    output_path: str = None,
):

    browser_config = browser_config or default_browser_config

    res = None
    content = None

    async with AsyncWebCrawler(config=browser_config) as crawler:
        crawl_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)

        res = await crawler.arun(
            url=url,
            config=crawl_config,
            session_id=session_id,
            timeout=15,
        )

    if not res.success:
        raise Crawler_NotSuccess(url=url, message=res.error_message)

    if output_path:
        content = res.markdown
        storage.save_to_disk(
            url=url, output_path=output_path, source=session_id, content=content
        )

    return res
