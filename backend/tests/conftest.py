import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from vaktmatch.config import Settings
from vaktmatch.main import create_app


@pytest.fixture
def data_dir(tmp_path: Path) -> Path:
    dataset = {"dataset": {"id": "test", "version": "1", "title": "Testdata"}}
    (tmp_path / "test.json").write_text(json.dumps(dataset), encoding="utf-8")
    return tmp_path


@pytest.fixture
def client(data_dir: Path) -> TestClient:
    return TestClient(create_app(Settings(data_dir=data_dir, _env_file=None)))
