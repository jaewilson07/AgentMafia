from fastapi import FastAPI, HTTPException
import requests
import routes.crawler as cw

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "API is running"}


@app.post("/api/crawl")
async def crawl_url(url: str, session_id="chrome_extension"):
    """
    Simple endpoint to crawl a URL and return its content.
    """
    try:

        res = await cw.crawl_url(url=url, session_id=session_id)
        return {
            "success": True,
            "url": url,
            "content": res.markdown,
            "status_code": 200
        }

    except cw.Crawler_NotSuccess as e:
        return {
            "success": False,
            "error": str(e),
            'url': url,
            "status_code": 500,
            "type": "crawler_error"
        }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
