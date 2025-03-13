from typing import List
import requests
from xml.etree import ElementTree
import asyncio
from rag.crawler import crawl_parallel

import sys

sys.path.append('.')


def get_pydantic_ai_docs_urls() -> List[str | None]:
    """Get URLs from Pydantic AI docs sitemap."""
    sitemap_url = "https://ai.pydantic.dev/sitemap.xml"
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()

        # Parse the XML
        root = ElementTree.fromstring(response.content)

        # Extract all URLs from the sitemap
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        return [loc.text for loc in root.findall('.//ns:loc', namespace)]

    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        return []


async def main():
    # Get URLs from Pydantic AI docs
    urls = get_pydantic_ai_docs_urls()
    if not urls:
        print("No URLs found to crawl")
        return

    print(f"Found {len(urls)} URLs to crawl")

    await crawl_parallel(urls=urls, session_id='pydantic_ai_docs')


if __name__ == "__main__":
    asyncio.run(main())
