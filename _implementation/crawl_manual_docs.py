import sys
import asyncio
import agent_mafia.implementations.scrape_urls as scu
import agent_mafia.routes.crawler as crawler_routes

sys.path.append(".")

domain_filter = crawler_routes.DomainFilter(allowed_domains=["api.slack.com"])

config = crawler_routes.CrawlerRunConfig(
    cache_mode=crawler_routes.CacheMode.ENABLED,
    deep_crawl_strategy=crawler_routes.BFSDeepCrawlStrategy(
        max_depth=1,
        filter_chain=crawler_routes.FilterChain([domain_filter]),
        include_external=False,
    ),
    stream=True,
    verbose=True,
)

await crawler_routes.crawl_urls(
    starting_url="https://api.slack.com/apis",
    session_id="slack_api_docs",
    crawler_config=config,
    storage_fn=partial(save_chunk_to_disk),
    output_path="../../TEST/crawler_routes/crawl/",
)


async def main():
    # Get URLs from Pydantic AI docs

    url = "https://api.slack.com/" or input("enter url:")
    source = "slack" or input("enter source:")

    await scu.process_urls(
        urls=[url], source=source, debug_prn=True, crawler_config=config
    )


if __name__ == "__main__":
    asyncio.run(main())
