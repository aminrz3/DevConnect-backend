from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(title="Devconnect Api")


@app.get("/health")
async def health_check():
    return {"status": "ok", "env": settings.ENV}
