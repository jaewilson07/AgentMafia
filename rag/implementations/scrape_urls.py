import os
from typing import List

import utils

from rag.routes import storage
from rag.routes import crawler
from rag.classes import ProcessedChunk as pc


async def process_chunk(
    url,
    chunk,
    chunk_number,
    source,
    supabase_client,
    database_table_name,
    export_folder,
    debug_prn: bool = False,
):
    try:
        if debug_prn:
            print(f"🎬 starting {url} - {chunk_number}")

        chunk_path = f"{export_folder}/chunks/{utils.convert_url_file_name(url)}/{chunk_number}.md"

        chunk = pc.ProcessedChunk.from_chunk(
            chunk=chunk,
            chunk_number=chunk_number,
            url=url,
            source=source,
            output_path=chunk_path,
        )

        await chunk.generate_metadata(output_path=chunk_path)

        data = chunk.to_json()
        data.pop("source")

        storage.store_data_in_supabase_table(
            supabase_client=supabase_client,
            table_name=database_table_name,
            data=data,
        )

        if debug_prn:
            print(f"successfully processed {url}-{chunk_number}")

        return chunk

    except Exception as e:
        print(f"💀 process_chunk - {url} - {chunk_number} -{e}")


async def read_url(url, source, browser_config, doc_path, debug_prn: bool = False):
    if os.path.exists(doc_path):
        content, _ = utils.read_md_from_disk(doc_path)

        if debug_prn:
            print(f"🛢️  {url} - scraping not required, file retrieved from - {doc_path}")

        return content

    res = await crawler.scrape_url(
        url=url,
        session_id=source,
        browser_config=browser_config,
        output_path=doc_path,
    )
    if debug_prn:
        print(f"🛢️  {url} - page scraped to {doc_path}")

    return res.markdown


async def process_url(
    url: str,
    source: str,
    export_folder: str,
    database_table_name: str,
    supabase_client=None,
    debug_prn: bool = False,
    browser_config=None,
    max_conccurent_requests=5,
):
    """process a document and store chunks in parallel"""

    browser_config = browser_config or crawler.default_browser_config
    supabase_client = supabase_client or storage.default_supabase_client

    doc_path = f"{export_folder}/{utils.convert_url_file_name(url)}.md"

    ## scrape url and save results to doc_path
    try:
        if debug_prn:
            print(f"starting crawl - {url}")

        markdown = await read_url(
            url=url,
            source=source,
            browser_config=browser_config,
            doc_path=doc_path,
            debug_prn=debug_prn,
        )

    except Exception as e:
        print(f"⛔  {url} - error while read_url - {e}")
        return False

    if debug_prn:
        print(f"☀️  successfully crawled: {url}")

    chunks = utils.chunk_text(markdown)

    if debug_prn:
        print(f"☀️  : {len(chunks)} to process {url}")

    res = await utils.gather_with_concurrency(
        *[
            process_chunk(
                url=url,
                chunk=chunk,
                chunk_number=idx,
                source=source,
                supabase_client=supabase_client,
                database_table_name=database_table_name,
                export_folder=export_folder,
                debug_prn=debug_prn,
            )
            for idx, chunk in enumerate(chunks)
        ],
        n=max_conccurent_requests,
    )

    if debug_prn:
        print(f"☀️  done processing url {url}")

    return res


async def process_urls(
    urls: List[str | None],
    source: str,
    export_folder: str = "./export",
    database_table_name: str = "site_pages",
    max_conccurent_requests: int = 5,
    debug_prn: bool = False,
    browser_config=None,
):
    if not urls:
        print("No URLs found to crawl")
        return

    urls_path = f"./export/urls/{source}.txt"

    utils.upsert_folder(urls_path)

    with open(urls_path, "w+", encoding="utf-8") as f:
        f.write("\n".join(urls))

    res = await utils.gather_with_concurrency(
        *[
            process_url(
                url=url,
                source=source,
                debug_prn=debug_prn,
                browser_config=browser_config,
                export_folder=export_folder,
                database_table_name=database_table_name,
            )
            for url in urls
        ],
        n=max_conccurent_requests,
    )

    print("done")
    return res
