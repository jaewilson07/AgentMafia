import streamlit as st
import asyncio
from crawler import get_pydantic_ai_docs_urls
from rag.crawler import crawl_parallel
import trafilatura
from typing import List
import requests
from xml.etree import ElementTree
<<<<<<< HEAD:main.py
=======
import asyncio
import src

>>>>>>> 5f899aa1ad9aae76fbc8bb83e655aa340b6de6cb:crawl_pydantic_ai_docs.py
import sys

sys.path.append(".")

st.set_page_config(
    page_title="Web Crawler App",
    page_icon="🕷️",
    layout="wide"
)

st.title("Web Crawler Application")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.header("Single URL Crawler")
    url = st.text_input("Enter a URL to crawl", placeholder="https://example.com")

    if st.button("Crawl Single URL"):
        if url:
            with st.spinner("Crawling..."):
                try:
                    # Download and extract content
                    downloaded = trafilatura.fetch_url(url)
                    text = trafilatura.extract(downloaded)
                    if text:
                        st.success("Crawling successful!")
                        st.text_area("Extracted Content", text, height=300)
                    else:
                        st.error("No content could be extracted from this URL")
                except Exception as e:
                    st.error(f"Error crawling URL: {str(e)}")
        else:
            st.warning("Please enter a URL")

with col2:
    st.header("Bulk URL Crawler")
    if st.button("Crawl Pydantic AI Docs"):
        with st.spinner("Getting URLs..."):
            urls = get_pydantic_ai_docs_urls()
            if urls:
                st.success(f"Found {len(urls)} URLs to crawl")
                st.write("URLs found:", urls[:5], "...")

                if st.button("Start Bulk Crawl"):
                    with st.spinner("Crawling all URLs..."):
                        try:
                            asyncio.run(crawl_parallel(urls=urls, session_id='pydantic_ai_docs'))
                            st.success("Bulk crawling completed!")
                        except Exception as e:
                            st.error(f"Error during bulk crawl: {str(e)}")
            else:
                st.error("No URLs found to crawl")

st.sidebar.title("About")
st.sidebar.info(
    """
    This web crawler application allows you to:
    1. Crawl a single URL and view its content
    2. Bulk crawl multiple URLs from Pydantic AI documentation

    The extracted content is cleaned and formatted for better readability.
    """
)


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
<<<<<<< HEAD:main.py
        return []
=======
        return []


async def main():
    # Get URLs from Pydantic AI docs
    urls = get_pydantic_ai_docs_urls()

    print(f"Found {len(urls)} URLs to crawl")

    await src.process_urls(
        urls=urls,
        source="pydantic_ai_docs",
        export_folder="./export",
        database_table_name="site_pages",
        debug_prn=True,
        max_conccurent_requests=5,
    )


if __name__ == "__main__":
    asyncio.run(main())
>>>>>>> 5f899aa1ad9aae76fbc8bb83e655aa340b6de6cb:crawl_pydantic_ai_docs.py
