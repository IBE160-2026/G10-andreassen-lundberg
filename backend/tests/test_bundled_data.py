from vaktmatch.config import DEFAULT_DATA_DIR
from vaktmatch.data import DatasetRepository


def test_bundled_datasets_are_valid():
    assert DatasetRepository(DEFAULT_DATA_DIR).list_datasets()
