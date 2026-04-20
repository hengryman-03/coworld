"""FastAPI entrypoint for CollabWorld backend."""

from fastapi import FastAPI

from app.api.routes import router
from app.core.config import get_settings

settings = get_settings()
app = FastAPI(title=settings.app_name)


@app.get("/health")
def health() -> dict[str, str]:
    """Simple health probe used by Docker and local smoke checks."""

    return {"status": "ok", "environment": settings.environment}


app.include_router(router, prefix=settings.api_prefix)
