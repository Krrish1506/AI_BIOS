"""Application configuration loaded from environment variables."""

import os
from enum import StrEnum
from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import Field, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# backend/app/config/settings.py → project root is four levels up
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
BACKEND_ROOT = PROJECT_ROOT / "backend"


class AppEnvironment(StrEnum):
    """Supported runtime environments."""

    DEVELOPMENT = "development"
    TESTING = "testing"
    PRODUCTION = "production"


def _resolve_env_files() -> tuple[str, ...]:
    """Load base .env then optional environment-specific overrides."""
    env_name = os.environ.get("APP_ENV", AppEnvironment.DEVELOPMENT)
    candidates: list[Path] = [
        PROJECT_ROOT / ".env",
        BACKEND_ROOT / ".env",
        PROJECT_ROOT / f".env.{env_name}",
        BACKEND_ROOT / f".env.{env_name}",
    ]
    return tuple(str(path) for path in candidates if path.is_file()) or (".env",)


class _EnvSettings(BaseSettings):
    """Shared pydantic-settings configuration for all setting groups."""

    model_config = SettingsConfigDict(
        env_file=_resolve_env_files(),
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
        populate_by_name=True,
    )


class ApplicationSettings(_EnvSettings):
    """Core application and API server settings."""

    app_name: str = Field(default="AI-BIOS", alias="APP_NAME")
    app_env: AppEnvironment = Field(
        default=AppEnvironment.DEVELOPMENT,
        alias="APP_ENV",
    )
    app_version: str = Field(default="1.0.0", alias="APP_VERSION")
    debug: bool = Field(default=True, alias="DEBUG")
    secret_key: str = Field(default="change-me", alias="SECRET_KEY")
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = Field(
        default="INFO",
        alias="LOG_LEVEL",
    )

    api_host: str = Field(default="0.0.0.0", alias="API_HOST")
    api_port: int = Field(default=8000, alias="API_PORT")
    api_prefix: str = Field(default="/api/v1", alias="API_PREFIX")
    allowed_origins: str = Field(
        default="http://localhost:3000",
        alias="ALLOWED_ORIGINS",
    )
    max_request_size_mb: int = Field(default=500, alias="MAX_REQUEST_SIZE_MB")

    @property
    def is_development(self) -> bool:
        return self.app_env == AppEnvironment.DEVELOPMENT

    @property
    def is_testing(self) -> bool:
        return self.app_env == AppEnvironment.TESTING

    @property
    def is_production(self) -> bool:
        return self.app_env == AppEnvironment.PRODUCTION

    @property
    def allowed_origins_list(self) -> list[str]:
        return [
            origin.strip()
            for origin in self.allowed_origins.split(",")
            if origin.strip()
        ]


class DatabaseSettings(_EnvSettings):
    """PostgreSQL connection and pool settings."""

    database_url: str = Field(
        default="postgresql+asyncpg://user:pass@localhost:5432/aibios",
        alias="DATABASE_URL",
    )
    database_pool_size: int = Field(default=10, alias="DATABASE_POOL_SIZE")
    database_max_overflow: int = Field(default=20, alias="DATABASE_MAX_OVERFLOW")
    database_pool_timeout: int = Field(default=30, alias="DATABASE_POOL_TIMEOUT")


class RedisSettings(_EnvSettings):
    """Redis cache and session store settings."""

    redis_url: str = Field(default="redis://localhost:6379/0", alias="REDIS_URL")
    redis_cache_ttl: int = Field(default=86400, alias="REDIS_CACHE_TTL")


class ChromaDBSettings(_EnvSettings):
    """ChromaDB vector store connection settings."""

    chroma_host: str = Field(default="localhost", alias="CHROMA_HOST")
    chroma_port: int = Field(default=8001, alias="CHROMA_PORT")
    chroma_collection_prefix: str = Field(
        default="aibios_",
        alias="CHROMA_COLLECTION_PREFIX",
    )

    @property
    def chroma_url(self) -> str:
        return f"http://{self.chroma_host}:{self.chroma_port}"


class GeminiSettings(_EnvSettings):
    """Google Gemini API settings."""

    gemini_api_key: str = Field(default="", alias="GEMINI_API_KEY")
    gemini_pro_model: str = Field(default="gemini-2.5-pro", alias="GEMINI_PRO_MODEL")
    gemini_flash_model: str = Field(
        default="gemini-2.5-flash",
        alias="GEMINI_FLASH_MODEL",
    )
    gemini_max_retries: int = Field(default=3, alias="GEMINI_MAX_RETRIES")
    gemini_timeout_seconds: int = Field(default=60, alias="GEMINI_TIMEOUT_SECONDS")
    gemini_max_output_tokens: int = Field(
        default=8192,
        alias="GEMINI_MAX_OUTPUT_TOKENS",
    )


class SecuritySettings(_EnvSettings):
    """Authentication, encryption, and security-related settings."""

    jwt_secret_key: str = Field(default="change-me", alias="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(default="HS256", alias="JWT_ALGORITHM")
    access_token_expire_minutes: int = Field(
        default=15,
        alias="ACCESS_TOKEN_EXPIRE_MINUTES",
    )
    refresh_token_expire_days: int = Field(
        default=7,
        alias="REFRESH_TOKEN_EXPIRE_DAYS",
    )
    password_hash_rounds: int = Field(default=12, alias="PASSWORD_HASH_ROUNDS")
    encryption_key: str = Field(default="", alias="ENCRYPTION_KEY")
    rate_limit_enabled: bool = Field(default=True, alias="RATE_LIMIT_ENABLED")
    rate_limit_storage_url: str = Field(
        default="redis://localhost:6379/3",
        alias="RATE_LIMIT_STORAGE_URL",
    )
    coa_approval_timeout_seconds: int = Field(
        default=300,
        alias="COA_APPROVAL_TIMEOUT_SECONDS",
    )
    coa_local_agent_ws_secret: str = Field(
        default="",
        alias="COA_LOCAL_AGENT_WS_SECRET",
    )


class Settings(
    ApplicationSettings,
    DatabaseSettings,
    RedisSettings,
    ChromaDBSettings,
    GeminiSettings,
    SecuritySettings,
):
    """Unified application configuration loaded from environment variables."""

    @field_validator("app_env", mode="before")
    @classmethod
    def normalize_app_env(cls, value: object) -> object:
        if isinstance(value, str):
            return value.lower()
        return value

    @model_validator(mode="after")
    def validate_environment_constraints(self) -> "Settings":
        if self.is_production and self.debug:
            raise ValueError("DEBUG must be false when APP_ENV is production")
        if self.is_production and self.secret_key == "change-me":
            raise ValueError("SECRET_KEY must be set when APP_ENV is production")
        if self.is_production and self.jwt_secret_key == "change-me":
            raise ValueError("JWT_SECRET_KEY must be set when APP_ENV is production")
        return self


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance (safe for FastAPI dependency injection)."""
    return Settings()


settings = get_settings()
