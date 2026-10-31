import json

import pytest

from vaktmatch.data import DatasetLoadError, DatasetNotFoundError, DatasetRepository


@pytest.mark.parametrize(
    "content",
    ["{", "[]", "{}", '{"dataset": {"id": "test"}}', '{"dataset": null}'],
)
def test_invalid_file_has_data_error_with_filename(tmp_path, content):
    (tmp_path / "invalid.json").write_text(content, encoding="utf-8")

    with pytest.raises(DatasetLoadError, match="invalid.json") as error:
        DatasetRepository(tmp_path).list_datasets()

    assert error.value.__cause__ is not None


def test_invalid_encoding_has_data_error(tmp_path):
    (tmp_path / "invalid.json").write_bytes(b"\xff")

    with pytest.raises(DatasetLoadError, match="invalid.json"):
        DatasetRepository(tmp_path).list_datasets()


def test_duplicate_ids_are_rejected(tmp_path):
    content = json.dumps({"dataset": {"id": "same", "version": "1", "title": "Test"}})
    for name in ("first.json", "second.json"):
        (tmp_path / name).write_text(content, encoding="utf-8")

    with pytest.raises(DatasetLoadError, match="Duplikat datasett-ID 'same'"):
        DatasetRepository(tmp_path).list_datasets()


@pytest.mark.parametrize("dataset_id", ["", "a/b"])
def test_ids_must_be_addressable_as_one_url_segment(tmp_path, dataset_id):
    content = json.dumps({"dataset": {"id": dataset_id, "version": "1", "title": "Test"}})
    (tmp_path / "invalid-id.json").write_text(content, encoding="utf-8")

    with pytest.raises(DatasetLoadError, match="invalid-id.json"):
        DatasetRepository(tmp_path).list_datasets()


def test_missing_directory_is_not_an_empty_catalog(tmp_path):
    with pytest.raises(DatasetLoadError, match="Datasettmappen finnes ikke"):
        DatasetRepository(tmp_path / "missing").list_datasets()


def test_unknown_id_keeps_its_distinct_error(data_dir):
    with pytest.raises(DatasetNotFoundError):
        DatasetRepository(data_dir).get_info("missing")
