"""Datatilgang: leser demodatasett og gir dem videre som validerte modeller.

Laget kjenner ikke regelmotoren eller API-et. Datamodellen utvides i SCRUM-19.
"""

from .repository import DatasetLoadError, DatasetNotFoundError, DatasetRepository
from .schema import DatasetInfo

__all__ = ["DatasetInfo", "DatasetLoadError", "DatasetNotFoundError", "DatasetRepository"]
