import sys
import asyncio
from functools import partial

import agent_mafia.routes.crawler as crawler_routes
import agent_mafia.routes.storage as storage_routes
from agent_mafia.implementations import scrape_urls


domain_filter = crawler_routes.DomainFilter(allowed_domains=["docs.slack.dev"])

browser_config = crawler_routes.BrowserConfig(
    browser_type="chromium",
    headless=True,
    verbose=True,
    extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
)


config = crawler_routes.CrawlerRunConfig(
    cache_mode=crawler_routes.CacheMode.BYPASS,
    deep_crawl_strategy=crawler_routes.BFSDeepCrawlStrategy(
        max_depth=1,
        filter_chain=crawler_routes.FilterChain([domain_filter]),
        include_external=False,
    ),
    stream=True,
    verbose=True,
)


async def main(debug_prn: bool = False):

    export_folder = "./export/slack_apis/"
    source = "slack_api_docs"

    res = await crawler_routes.crawl_urls(
        starting_url="https://docs.slack.dev/apis/",
        crawler_config=config,
        browser_config=browser_config,
        session_id=source,
        storage_fn=storage_routes.save_chunk_to_disk,
        process_fn=partial(scrape_urls.process_rgd, source=source),
        output_folder=export_folder,
    )

    # for rgd in res:
    #     await scrape_urls.process_rgd(
    #         rgd=rgd, export_folder=export_folder, source=source, debug_prn=True
    #     )

    return res


if __name__ == "__main__":
    asyncio.run(main())
