from supabase import create_client, Client
import os
import utils
import json
import datetime as dt
from frontmatter import Frontmatter

default_supabase_client: Client = create_client(
    os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_KEY")
)


def store_data_in_supabase_table(
    table_name,
    data,
    supabase_client: Client = None,
):
    supabase_client = supabase_client or default_supabase_client
    return (
        supabase_client.table(table_name)
        .upsert(data, on_conflict="url, chunk_number")
        .execute()
    )


def save_to_disk(
    output_path,
    url,
    source,
    content,
    title=None,
    summary=None,
    embedding=None,
    metadata=None,
    chunk_number=None,
    **kwargs,
):

    utils.upsert_folder(output_path)

    output_str = ["---"]

    if url:
        output_str.append(f"url: {url}")
    if source:
        output_str.append(f"session_id: {source}")
    if chunk_number is not None:
        output_str.append(f"chunk_number: {chunk_number}")
    if title:
        output_str.append(f"title: {title}")
    if summary:
        output_str.append(f"summary: {summary}")
    if embedding:
        output_str.append(f"embedding: {embedding}")
    if metadata:
        output_str.append(f"metadata : {json.dumps(metadata)}")
    output_str.append(f"updated_dt: {dt.datetime.now().isoformat()}")
    output_str.append("---")
    output_str.append(content)

    with open(output_path, "w+", encoding="utf-8") as f:
        f.write("\n".join(output_str))

        return True
