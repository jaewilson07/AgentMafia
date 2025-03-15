from typing import List
import requests
from xml.etree import ElementTree
import asyncio
import rag

import sys

sys.path.append(".")


def get_pydantic_ai_docs_urls() -> List[str | None]:
    """Get URLs from Pydantic AI docs sitemap."""
    sitemap_url = "https://ai.pydantic.dev/sitemap.xml"
    try:
        response = requests.get(sitemap_url, timeout=5)
        response.raise_for_status()

        # Parse the XML
        root = ElementTree.fromstring(response.content)

        # Extract all URLs from the sitemap
        namespace = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        return [loc.text for loc in root.findall(".//ns:loc", namespace)]

    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        return []


async def main():
    # Get URLs from Pydantic AI docs
    urls = get_pydantic_ai_docs_urls()

    print(f"Found {len(urls)} URLs to crawl")

    await rag.process_urls(
        urls=urls,
        source="pydantic_ai_docs",
        export_folder="./export",
        database_table_name="site_pages",
        debug_prn=True,
        max_conccurent_requests=5,
    )


if __name__ == "__main__":
    asyncio.run(main())
