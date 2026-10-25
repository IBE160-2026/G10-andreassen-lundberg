import json
from pathlib import Path

from .schema import DatasetInfo


class DatasetNotFoundError(LookupError):
    pass


class DatasetRepository:
    """Leser datasett fra JSON-filer i én mappe. Filene endres aldri herfra."""

    def __init__(self, data_dir: Path) -> None:
        self._data_dir = data_dir

    def list_datasets(self) -> list[DatasetInfo]:
        return [self._read_info(path) for path in sorted(self._data_dir.glob("*.json"))]

    def get_info(self, dataset_id: str) -> DatasetInfo:
        for info in self.list_datasets():
            if info.id == dataset_id:
                return info
        raise DatasetNotFoundError(dataset_id)

    @staticmethod
    def _read_info(path: Path) -> DatasetInfo:
        raw = json.loads(path.read_text(encoding="utf-8"))
        return DatasetInfo.model_validate(raw["dataset"])
