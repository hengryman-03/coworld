"""Application configuration for backend service.

This module exists to keep environment parsing in one place so routes/services
can depend on a stable typed settings object.
"""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    """Runtime configuration needed by initial project phases."""

    app_name: str = "CollabWorld API"
    api_prefix: str = "/api/v1"
    environment: str = "development"


def get_settings() -> Settings:
    """Build settings from environment variables with safe defaults."""

    return Settings(
        app_name=os.getenv("APP_NAME", "CollabWorld API"),
        api_prefix=os.getenv("API_PREFIX", "/api/v1"),
        environment=os.getenv("APP_ENV", "development"),
    )
