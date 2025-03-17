import uvicorn

from agent_mafia.routes.api import app

if __name__ == "__main__":
    uvicorn.run(
        "src.routes.api:app",
        host="0.0.0.0",
        port=5000,
        reload=True
    )