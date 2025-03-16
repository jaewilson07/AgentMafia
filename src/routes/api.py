from fastapi import FastAPI, HTTPException

from src.routes import crawler
from src.implementations import scrape_urls

app = FastAPI()


@app.post("/api/crawl")
async def crawl_url(
    url: str,
    session_id: str = "default_session",
    export_folder: str = "./export",
    database_table_name: str = "site_pages",
):
    try:
        result = await scrape_urls.process_url(
            url=url,
            source=session_id,
            export_folder=export_folder,
            database_table_name=database_table_name,
            debug_prn=True,
        )

        return {
            "success": True,
            "message": f"Successfully processed {url}",
            "result": result,
        }

    except crawler.Crawler_NotSuccess as e:
        raise HTTPException(
            status_code=500, detail={"error": str(e), "type": "crawler_error"}
        ) from e

    except Exception as e:
        raise HTTPException(
            status_code=500, detail={"error": str(e), "type": "server_error"}
        ) from e
