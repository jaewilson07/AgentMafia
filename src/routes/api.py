from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.post("/api/crawl")
async def crawl_url(url: str):
    """
    Simple endpoint to crawl a URL and return its content.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        return {
            "success": True,
            "url": url,
            "content": response.text,
            "status_code": response.status_code
        }

    except requests.RequestException as e:
        raise HTTPException(
            status_code=400,
            detail={
                "error": str(e),
                "type": "crawler_error"
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "error": str(e),
                "type": "server_error"
            }
        )