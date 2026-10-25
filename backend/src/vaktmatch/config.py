"""Innstillinger fra miljøvariabler. Hemmeligheter leses aldri fra repoet."""

from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

DEFAULT_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "datasets"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="VAKTMATCH_", env_file=".env", extra="ignore")

    data_dir: Path = DEFAULT_DATA_DIR
    # Tom verdi gir regelbaserte forklaringer. Leverandør velges i SCRUM-59.
    llm_provider: str = ""
    llm_api_key: SecretStr | None = None
    cors_origins: list[str] = ["http://localhost:5173"]


def get_settings() -> Settings:
    return Settings()
