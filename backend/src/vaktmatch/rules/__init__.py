"""Regelmotor: kontrollerer kandidater mot scenarioreglene R1–R5.

Ren beregning uten avhengighet til web, lagring eller KI. Selve reglene
implementeres i SCRUM-24–27; se docs/demoscenario-fravaer.md.
"""

from .status import ControlStatus

__all__ = ["ControlStatus"]
