from ..rules import ControlStatus
from .base import Explanation

_SUMMARIES = {
    ControlStatus.PASSED: "Kandidaten oppfyller scenarioreglene i dette datagrunnlaget.",
    ControlStatus.RULE_VIOLATION: "Minst én scenarioregel er brutt.",
    ControlStatus.UNRESOLVED: "Nødvendige opplysninger mangler, så kontrollen er ikke fullført.",
}


class RuleBasedExplainer:
    """Standardforklaringer uten språkmodell (SCRUM-40)."""

    name = "regelbasert"

    def explain(self, status: ControlStatus) -> Explanation:
        return Explanation(source=self.name, summary=_SUMMARIES[status])
