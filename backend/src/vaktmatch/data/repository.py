import json
from pathlib import Path

from pydantic import ValidationError

from .schema import DatasetInfo


class DatasetNotFoundError(LookupError):
    pass


class DatasetLoadError(ValueError):
    """Datagrunnlaget kan ikke brukes; API-kontrakten håndteres i SCRUM-22."""


class DatasetRepository:
    """Leser datasett fra JSON-filer i én mappe. Filene endres aldri herfra."""

    def __init__(self, data_dir: Path) -> None:
        self._data_dir = data_dir

    def list_datasets(self) -> list[DatasetInfo]:
        if not self._data_dir.is_dir():
            raise DatasetLoadError(f"Datasettmappen finnes ikke: {self._data_dir}")
        datasets = []
        seen = set()
        for path in sorted(self._data_dir.glob("*.json")):
            info = self._read_info(path)
            if info.id in seen:
                raise DatasetLoadError(f"Duplikat datasett-ID {info.id!r} i {path.name}")
            seen.add(info.id)
            datasets.append(info)
        return datasets

    def get_info(self, dataset_id: str) -> DatasetInfo:
        for info in self.list_datasets():
            if info.id == dataset_id:
                return info
        raise DatasetNotFoundError(dataset_id)

    @staticmethod
    def _read_info(path: Path) -> DatasetInfo:
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(raw, dict):
                raise ValueError("JSON-roten må være et objekt")
            return DatasetInfo.model_validate(raw["dataset"])
        except (OSError, UnicodeError, ValueError, KeyError, ValidationError) as error:
            raise DatasetLoadError(
                f"Kan ikke lese gyldige datasettmetadata fra {path.name}"
            ) from error
