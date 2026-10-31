"""Innstillinger fra miljøvariabler. Hemmeligheter leses aldri fra repoet."""

from pathlib import Path

from pydantic import SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DATA_DIR = BACKEND_ROOT / "data" / "datasets"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="VAKTMATCH_", env_file=".env", extra="ignore")

    data_dir: Path = DEFAULT_DATA_DIR
    # Tom verdi gir regelbaserte forklaringer. Leverandør velges i SCRUM-59.
    llm_provider: str = ""
    llm_api_key: SecretStr | None = None
    cors_origins: list[str] = ["http://localhost:5173"]

    @field_validator("data_dir")
    @classmethod
    def anchor_data_dir(cls, value: Path) -> Path:
        return value if value.is_absolute() else (BACKEND_ROOT / value).resolve()


def get_settings() -> Settings:
    return Settings()
