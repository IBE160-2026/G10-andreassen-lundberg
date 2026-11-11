from pydantic import SecretStr

from vaktmatch.config import DEFAULT_DATA_DIR, Settings
from vaktmatch.data import DatasetRepository
from vaktmatch.data.schema import Absence
from vaktmatch.explain import RuleBasedExplainer, get_explainer
from vaktmatch.explain.demoflow import compare_explanation, standard_explanation
from vaktmatch.rules import ControlStatus
from vaktmatch.rules.engine import evaluate


def test_every_status_has_a_rule_based_explanation():
    explainer = RuleBasedExplainer()
    for status in ControlStatus:
        assert explainer.explain(status).summary


def test_unknown_provider_falls_back_to_rule_based():
    settings = Settings(llm_provider="ukjent", llm_api_key=SecretStr("x"), _env_file=None)
    assert get_explainer(settings).name == "regelbasert"


def test_proposal_failure_identifies_replacement_without_mislabeling_main_candidate():
    dataset = DatasetRepository(DEFAULT_DATA_DIR).get_dataset("en-flytting")
    result = evaluate(dataset, [Absence(employee_id="A", shift_id="X")], "X", 1)
    proposal = next(
        a
        for a in result["alternatives"]
        if a["candidate_id"] == "B" and a["affected_employee_ids"] == ["B", "F04"]
    )
    assert (
        next(p for p in proposal["consequences"] if p["employee_id"] == "B")["control_status"]
        == "bestatt"
    )
    text = standard_explanation(proposal)["short_answer"]
    assert "Forslaget med B har regelavvik" in text
    assert "F04: R1 (regelavvik)" in text
    assert "B: R1" not in text


def test_missing_p2_is_readable_and_appears_in_uncertainty():
    dataset = DatasetRepository(DEFAULT_DATA_DIR).get_dataset("mangler-p2")
    result = evaluate(dataset, [Absence(employee_id="A01", shift_id="X")], "X", 0, ["P2"])
    candidate = next(a for a in result["alternatives"] if a["candidate_id"] == "A03")
    reference = next(a for a in result["alternatives"] if a["rank"] == 1)
    text = compare_explanation(candidate, reference, ["P2"])
    assert "uavklart andel av avtalte timer" in text["tradeoff"]
    assert "133,3 % av avtalte timer" in text["tradeoff"]
    assert "None" not in text["tradeoff"]
    assert "1.33333" not in text["tradeoff"]
    assert "P2: nødvendig timetall mangler" in text["uncertainty"]
