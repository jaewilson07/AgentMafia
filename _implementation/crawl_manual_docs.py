
import asyncio
import agent_mafia.implementations.scrape_urls as scu
import sys

from crawl4ai import CrawlerRunConfig, CacheMode
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.deep_crawling.filters import FilterChain, DomainFilter
from crawl4ai import CrawlerRunConfig

sys.path.append(".")

# url_filter = URLPatternFilter(patterns=["*blog*", "*docs*"])

domain_filter = (
    DomainFilter(
        allowed_domains=["api.slack.com"],
        # blocked_domains=["old.docs.example.com"]
    ),
)

config = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,
    deep_crawl_strategy=BFSDeepCrawlStrategy(
        max_depth=1, filter_chain=FilterChain([domain_filter])
    ),
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
