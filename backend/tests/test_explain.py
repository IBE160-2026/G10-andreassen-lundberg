from pydantic import SecretStr

from vaktmatch.config import Settings
from vaktmatch.explain import RuleBasedExplainer, get_explainer
from vaktmatch.rules import ControlStatus


def test_every_status_has_a_rule_based_explanation():
    explainer = RuleBasedExplainer()
    for status in ControlStatus:
        assert explainer.explain(status).summary


def test_unknown_provider_falls_back_to_rule_based():
    settings = Settings(llm_provider="ukjent", llm_api_key=SecretStr("x"), _env_file=None)
    assert get_explainer(settings).name == "regelbasert"
