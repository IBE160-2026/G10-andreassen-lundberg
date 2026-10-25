"""Forklaringer av kontrollresultater i fast svarformat.

Forklaringen leser bare ferdige kontrollresultater og kan aldri endre status,
rangering eller lederens valg. Regelbasert forklaring er standard og brukes
også når en språkmodell mangler nøkkel eller feiler.
"""

from .base import Explainer, Explanation
from .factory import get_explainer
from .rule_based import RuleBasedExplainer

__all__ = ["Explainer", "Explanation", "RuleBasedExplainer", "get_explainer"]
