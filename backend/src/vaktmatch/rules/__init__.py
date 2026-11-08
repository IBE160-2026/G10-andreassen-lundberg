"""Regelmotor: kontrollerer kandidater mot scenarioreglene R1–R5.

Ren beregning uten avhengighet til web, lagring eller KI. engine.py leverer
R1–R5, P1/P2, søkegrense 0/1, historikk og syntetisk kostnad.
"""

from .status import ControlStatus

__all__ = ["ControlStatus"]
