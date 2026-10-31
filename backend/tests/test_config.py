import os

import pytest

from vaktmatch.config import BACKEND_ROOT, DEFAULT_DATA_DIR, Settings


@pytest.fixture(autouse=True)
def isolate_settings_environment(monkeypatch):
    for name in os.environ:
        if name.startswith("VAKTMATCH_"):
            monkeypatch.delenv(name)


def test_prefixed_environment_overrides_dotenv(tmp_path, monkeypatch):
    env_file = tmp_path / ".env"
    env_file.write_text("VAKTMATCH_LLM_PROVIDER=from-file\n", encoding="utf-8")
    assert Settings(_env_file=env_file).llm_provider == "from-file"

    monkeypatch.setenv("LLM_PROVIDER", "unprefixed")
    assert Settings(_env_file=None).llm_provider == ""
    monkeypatch.setenv("VAKTMATCH_LLM_PROVIDER", "from-environment")
    assert Settings(_env_file=env_file).llm_provider == "from-environment"


def test_json_cors_list_from_environment(monkeypatch):
    monkeypatch.setenv("VAKTMATCH_CORS_ORIGINS", '["http://localhost:9999"]')
    assert Settings(_env_file=None).cors_origins == ["http://localhost:9999"]


def test_relative_data_directory_is_anchored_to_backend(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("VAKTMATCH_DATA_DIR", "data/datasets")

    assert Settings(_env_file=None).data_dir == DEFAULT_DATA_DIR


def test_absolute_data_directory_is_preserved(tmp_path):
    assert Settings(data_dir=tmp_path, _env_file=None).data_dir == tmp_path


def test_example_has_no_credentials_and_loads_without_key(tmp_path):
    text = (BACKEND_ROOT / ".env.example").read_text(encoding="utf-8")
    active = [line for line in text.splitlines() if line and not line.startswith("#")]
    assert active == ["VAKTMATCH_LLM_PROVIDER=", "VAKTMATCH_LLM_API_KEY="]
    env_file = tmp_path / ".env"
    env_file.write_text(text, encoding="utf-8")

    settings = Settings(_env_file=env_file)

    assert settings.llm_provider == ""
    assert settings.llm_api_key is None or settings.llm_api_key.get_secret_value() == ""
    assert settings.data_dir == DEFAULT_DATA_DIR
