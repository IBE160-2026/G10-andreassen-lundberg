"""Datatilgang: leser demodatasett og gir dem videre som validerte modeller.

Laget kjenner ikke regelmotoren eller API-et. Fullmodellen validerer
tidssoner, intervaller, satser, unike ID-er og alle referanser.
"""

from .repository import DatasetLoadError, DatasetNotFoundError, DatasetRepository
from .schema import DatasetInfo

__all__ = ["DatasetInfo", "DatasetLoadError", "DatasetNotFoundError", "DatasetRepository"]
