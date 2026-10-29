import logging

from ..config import Settings
from .base import Explainer
from .rule_based import RuleBasedExplainer

logger = logging.getLogger(__name__)


def get_explainer(settings: Settings) -> Explainer:
    """Velger forklaringstjeneste. Uten gyldig leverandør og nøkkel brukes regelbasert."""
    if settings.llm_provider and settings.llm_api_key:
        # Ingen leverandør er valgt ennå (SCRUM-59).
        logger.warning(
            "Ukjent språkmodell %r; bruker regelbasert forklaring", settings.llm_provider
        )
    return RuleBasedExplainer()
