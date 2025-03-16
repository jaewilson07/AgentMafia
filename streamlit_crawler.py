import streamlit as st
import asyncio
from src import process_url


async def main():

    st.set_page_config(page_title="Web Crawler App", page_icon="🕷️", layout="wide")

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

                        await process_url(
                            url,
                            source="manual scrape",
                            export_folder="./export",
                            database_table_name="site_pages",
                            debug_prn=True,
                        )

                        st.success("Crawling successful!")

                    except Exception as e:
                        st.error(f"Error crawling URL: {str(e)}")
            else:
                st.warning("Please enter a URL")

    with col2:
        pass
    #     st.header("Bulk URL Crawler")
    #     if st.button("Crawl Pydantic AI Docs"):
    #         with st.spinner("Getting URLs..."):
    #             urls = get_pydantic_ai_docs_urls()
    #             if urls:
    #                 st.success(f"Found {len(urls)} URLs to crawl")
    #                 st.write("URLs found:", urls[:5], "...")

    #                 if st.button("Start Bulk Crawl"):
    #                     with st.spinner("Crawling all URLs..."):
    #                         try:
    #                             asyncio.run(
    #                                 crawl_parallel(urls=urls, session_id="pydantic_ai_docs")
    #                             )
    #                             st.success("Bulk crawling completed!")
    #                         except Exception as e:
    #                             st.error(f"Error during bulk crawl: {str(e)}")
    #             else:
    #                 st.error("No URLs found to crawl")

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This web crawler application allows you to:
        1. Crawl a single URL and view its content
        2. Bulk crawl multiple URLs from Pydantic AI documentation

        The extracted content is cleaned and formatted for better readability.
        """
    )


if __name__ == "__main__":
    asyncio.run(main())
