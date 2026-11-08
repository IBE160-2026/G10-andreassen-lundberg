from copy import deepcopy
from datetime import datetime, timedelta
from decimal import Decimal
from zoneinfo import ZoneInfo

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from vaktmatch.config import DEFAULT_DATA_DIR, Settings
from vaktmatch.data import DatasetRepository
from vaktmatch.data.schema import Absence, Assignment, Dataset, Interval, Shift, Supplement
from vaktmatch.main import create_app
from vaktmatch.rules.engine import (
    active_plan,
    available,
    cost_assignment,
    evaluate,
    history,
    hours,
    overlap,
    week_hours,
)


@pytest.fixture
def repository():
    return DatasetRepository(DEFAULT_DATA_DIR)


@pytest.fixture
def demo_client():
    return TestClient(create_app(Settings(_env_file=None)))


def run(dataset, limit=0, criteria=None):
    eid = "A" if dataset.dataset.family_id == "flytting" else "A01"
    return evaluate(dataset, [Absence(employee_id=eid, shift_id="X")], "X", limit, criteria)


def direct(result, eid):
    return next(a for a in result["alternatives"] if a["candidate_id"] == eid and not a["moves"])


def test_all_bundled_full_datasets_validate(repository):
    assert len(repository.list_datasets()) == 11
    for info in repository.list_datasets():
        assert repository.get_dataset(info.id).dataset == info


def test_main_oracle_and_sorting_without_mutation(repository):
    dataset = repository.get_dataset("hovedscenario")
    original = dataset.model_dump_json()
    result = run(dataset)
    assert [(a["candidate_id"], a["rank"]) for a in result["alternatives"] if a["rank"]] == [
        ("A02", 1),
        ("A03", 2),
    ]
    expected = {
        "A02": (24, 32, 16, 16),
        "A03": (32, 40, 12, 16),
        "A04": (24, 32, 16, 16),
        "A05": (24, 32, 8, 16),
        "A06": (24, 32, 16, 4),
        "A07": (24, 32, 16, 16),
        "A08": (40, 48, 16, 16),
        "V01": (16, 24, 16, 16),
    }
    for eid, (before, after, rest_before, rest_after) in expected.items():
        alternative = direct(result, eid)
        person = alternative["consequences"][0]
        assert (person["hours_before"], person["hours_after"]) == (before, after)
        assert (
            person["rest_after"][0]["before_hours"],
            person["rest_after"][0]["after_hours"],
        ) == (rest_before, rest_after)
        assert alternative["control_status"] == (
            "bestatt" if eid in ("A02", "A03") else "uavklart" if eid == "V01" else "regelavvik"
        )
    assert direct(result, "A07")["consequences"][0]["rules"][3]["status"] == "ikke_vurdert"
    p2 = run(dataset, criteria=["P2"])
    assert p2["alternatives"][0]["candidate_id"] == "A03"
    assert {a["id"] for a in result["alternatives"]} == {a["id"] for a in p2["alternatives"]}
    assert dataset.model_dump_json() == original


@pytest.mark.parametrize(
    "identifier,passed", [("ingen-direkte", []), ("mangler", []), ("mangler-komplettert", ["V01"])]
)
def test_missing_and_completed_data(repository, identifier, passed):
    result = run(repository.get_dataset(identifier))
    assert [a["candidate_id"] for a in result["alternatives"] if a["selectable"]] == passed


def test_ties_and_missing_p2(repository):
    result = run(repository.get_dataset("lik-rang"), criteria=["P1", "P2"])
    assert direct(result, "A02")["rank"] == direct(result, "A03")["rank"] == 1
    result = run(repository.get_dataset("mangler-p2"), criteria=["P2"])
    assert direct(result, "A03")["control_status"] == "bestatt"
    assert direct(result, "A03")["rank"] is None
    assert direct(result, "A03")["sorting_missing"]


def test_one_move_and_exact_cost_o1_o2(repository):
    dataset = repository.get_dataset("en-flytting")
    assert not any(a["selectable"] for a in run(dataset)["alternatives"])
    result = run(dataset, 1)
    best = next(a for a in result["alternatives"] if a["selectable"])
    assert best["candidate_id"] == "B"
    assert best["moves"] == 1
    assert best["affected_employee_ids"] == ["B", "C"]
    assert best["plan"] == [
        {"shift_id": "X", "before": [], "after": ["B"]},
        {"shift_id": "Y", "before": ["B"], "after": ["C"]},
    ]
    assert (best["cost"]["total"], best["cost"]["reference"], best["cost"]["difference"]) == (
        3240,
        1600,
        1640,
    )
    direct_cost = direct(run(repository.get_dataset("hovedscenario")), "A02")["cost"]
    assert (direct_cost["total"], direct_cost["reference"], direct_cost["difference"]) == (
        1800,
        0,
        1800,
    )


def test_missing_replacement_partial_and_locks(repository):
    dataset = repository.get_dataset("udekket-y")
    result = run(dataset, 1)
    assert not any(a["selectable"] for a in result["alternatives"])
    partial = next(
        a for a in result["alternatives"] if a["kind"] == "delvis" and a["candidate_id"] == "B"
    )
    assert partial["uncovered"][0]["shift_id"] == "Y"
    dataset.assignments[1].locked = True
    assert not any(a["moves"] for a in run(dataset, 1)["alternatives"])
    dataset.assignments[0].locked = True
    assert run(dataset)["search_status"] == "fullfort"


def test_missing_rate_preserves_rule_status_o3(repository):
    dataset = repository.get_dataset("en-flytting")
    dataset.employees[2].hourly_rate = None
    best = next(a for a in run(dataset, 1)["alternatives"] if a["selectable"])
    assert best["cost"]["total"] is None and best["cost"]["difference"] is None
    assert best["cost"]["known_subtotal"] == 1800


def test_interval_supplement_and_assignment_rounding_o5(repository):
    dataset = repository.get_dataset("hovedscenario")
    shift = next(s for s in dataset.shifts if s.id == "X")
    dataset.supplements = [
        Supplement(start=shift.start, end=shift.start + timedelta(hours=2), rate=25, shift_id="X")
    ]
    assignment = Assignment(id="cost", employee_id="A02", shift_id="X")
    assert cost_assignment(dataset, assignment)["amount"] == 1650
    shift.end = shift.start + timedelta(hours=1)
    dataset.supplements = []
    dataset.employees[1].hourly_rate = Decimal("200.005")
    assert cost_assignment(dataset, assignment)["amount"] == Decimal("200.01")
    dataset.supplements = None
    assert cost_assignment(dataset, assignment)["amount"] is None


def test_known_violation_precedes_missing_work_and_skills(repository):
    dataset = repository.get_dataset("hovedscenario")
    employee = dataset.employees[7]
    employee.work_context_complete = False
    employee.skills = None
    candidate = direct(run(dataset), "A08")
    assert candidate["control_status"] == "regelavvik"
    assert candidate["p1"] is None
    assert candidate["consequences"][0]["rules"][-1]["status"] == "regelavvik"


@pytest.mark.parametrize("rest, expected", [(11, "bestatt"), (10, "regelavvik")])
def test_exact_rest_boundary(repository, rest, expected):
    dataset = repository.get_dataset("hovedscenario")
    shift = next(s for s in dataset.shifts if s.id == "W5-A02-2")
    shift.end = next(s for s in dataset.shifts if s.id == "X").start - timedelta(hours=rest)
    shift.start = shift.end - timedelta(hours=8)
    assert direct(run(dataset), "A02")["control_status"] == expected


def test_adjacent_availability_and_no_overlap_at_equal_end(repository):
    dataset = repository.get_dataset("hovedscenario")
    shift = next(s for s in dataset.shifts if s.id == "X")
    midpoint = shift.start + timedelta(hours=4)
    dataset.employees[1].availability = [
        Interval(start=shift.start, end=midpoint),
        Interval(start=midpoint, end=shift.end),
    ]
    assert available(dataset.employees[1], shift)
    assert not overlap(
        Interval(start=shift.start, end=midpoint), Interval(start=midpoint, end=shift.end)
    )


def test_utc_duration_dst_and_partial_week(repository):
    oslo = ZoneInfo("Europe/Oslo")
    assert (
        hours(datetime(2026, 10, 25, 0, tzinfo=oslo), datetime(2026, 10, 25, 8, tzinfo=oslo)) == 9
    )
    dataset = repository.get_dataset("hovedscenario")
    night = Shift(
        id="night",
        start=dataset.week_end - timedelta(hours=2),
        end=dataset.week_end + timedelta(hours=6),
        required_skill="K1",
        required_count=1,
    )
    dataset.shifts.append(night)
    dataset.assignments.append(Assignment(id="night-A02", employee_id="A02", shift_id="night"))
    assert week_hours(dataset, "A02", active_plan(dataset, [])) == 26
    result = evaluate(dataset, [Absence(employee_id="A02", shift_id="night")], "night", 0)
    assert result["search_status"] == "fullfort"


@pytest.mark.parametrize("change", ["naive", "duplicate", "reference", "negative", "shortweek"])
def test_invalid_full_models_rejected(repository, change):
    raw = repository.get_dataset("hovedscenario").model_dump(mode="json")
    if change == "naive":
        raw["shifts"][0]["start"] = "2026-09-15T08:00:00"
    if change == "duplicate":
        raw["employees"].append(deepcopy(raw["employees"][0]))
    if change == "reference":
        raw["assignments"][0]["employee_id"] = "missing"
    if change == "negative":
        raw["employees"][0]["hourly_rate"] = "-1"
    if change == "shortweek":
        raw["week_end"] = "2026-10-18T23:00:00+02:00"
    with pytest.raises(ValidationError):
        Dataset.model_validate(raw)


def body(identifier="hovedscenario", employee="A01"):
    return {
        "dataset_id": identifier,
        "version": "1.0",
        "absences": [{"employee_id": employee, "shift_id": "X"}],
        "target_shift_id": "X",
        "search_limit": 0,
        "criteria": ["P1"],
    }


def test_api_absence_idempotence_and_unchanged_source(demo_client):
    original = demo_client.get("/api/datasets/hovedscenario/state").json()
    payload = {
        k: v for k, v in body().items() if k not in ("target_shift_id", "search_limit", "criteria")
    }
    payload["absences"] = []
    payload["absence"] = {"employee_id": "A01", "shift_id": "X"}
    first = demo_client.post("/api/absences/simulate", json=payload)
    assert first.status_code == 200
    payload["absences"] = first.json()["absences"]
    second = demo_client.post("/api/absences/simulate", json=payload)
    assert len(second.json()["absences"]) == 1
    assert demo_client.get("/api/datasets/hovedscenario/state").json() == original


def test_api_errors_stale_absences_and_explanation(demo_client):
    payload = body()
    payload["version"] = "old"
    assert demo_client.post("/api/evaluate", json=payload).status_code == 409
    payload = body()
    payload["target_shift_id"] = "no"
    assert demo_client.post("/api/evaluate", json=payload).status_code == 422
    payload = body()
    payload["absences"].append({"employee_id": "A02", "shift_id": "H4-A02"})
    assert demo_client.post("/api/evaluate", json=payload).status_code == 422
    payload = body()
    payload["criteria"] = []
    assert demo_client.post("/api/evaluate", json=payload).status_code == 422
    result = demo_client.post("/api/evaluate", json=body()).json()
    assert result["alternatives"][0]["cost"]["total"] == "1800.00"
    explanation = demo_client.post(
        "/api/explain", json={**body(), "alternative_id": result["alternatives"][1]["id"]}
    ).json()
    assert explanation["mode"] == "standard" and explanation["reference_id"]
    assert "KI-forklaring er ikke tilgjengelig" in explanation["message"]


def test_api_dataset_updates_and_out_of_scope(demo_client):
    result = demo_client.post(
        "/api/datasets/compare", json={"previous_id": "hovedscenario", "next_id": "oppdatert-plan"}
    ).json()
    assert any(c["field"] == "hourly_rate" for c in result["changes"])
    assert any(c["category"] == "assignments" for c in result["changes"])
    result = demo_client.post(
        "/api/datasets/compare", json={"previous_id": "hovedscenario", "next_id": "uendret"}
    ).json()
    assert result["unchanged"]
    payload = body("oppdatert-plan")
    payload["version"] = "2.1"
    assert (
        demo_client.post("/api/evaluate", json=payload).json()["search_status"] == "utenfor_omfang"
    )
    payload = body()
    payload["target_shift_id"] = "W5-A02-1"
    assert (
        demo_client.post("/api/evaluate", json=payload).json()["search_status"] == "utenfor_omfang"
    )


def test_preview_and_invalid_absence(demo_client):
    base = {"dataset_id": "hovedscenario", "version": "1.0", "absences": []}
    result = demo_client.post(
        "/api/absences/preview",
        json={**base, "employee_id": "A01", "start_shift_id": "X", "calendar_days": 3},
    ).json()
    assert [a["shift"]["id"] for a in result["affected"]] == ["X", "W5-A01-2"]
    assert (
        demo_client.post(
            "/api/absences/simulate",
            json={**base, "absence": {"employee_id": "A02", "shift_id": "W5-A02-1"}},
        ).status_code
        == 422
    )
    assert (
        demo_client.post(
            "/api/absences/simulate",
            json={**base, "absence": {"employee_id": "no", "shift_id": "X"}},
        ).status_code
        == 422
    )


@pytest.mark.parametrize(
    "previous_end,complete,expected",
    [(21, True, "bestatt"), (22, True, "regelavvik"), (21, False, "uavklart")],
)
def test_h5_week_start_requires_known_neighbor_context(
    repository, previous_end, complete, expected
):
    dataset = repository.get_dataset("en-flytting")
    target = next(s for s in dataset.shifts if s.id == "X")
    target.start = dataset.week_start + timedelta(hours=8)
    target.end = target.start + timedelta(hours=8)
    dataset.assessment_time = dataset.week_start + timedelta(hours=7)
    last = Shift(
        id="week4-last",
        start=dataset.week_start - timedelta(hours=12),
        end=dataset.week_start - timedelta(hours=24 - previous_end),
        required_skill="K1",
        required_count=1,
    )
    dataset.shifts.append(last)
    dataset.assignments.append(
        Assignment(id="last-B", employee_id="B", shift_id=last.id, locked=True)
    )
    dataset.employees[1].work_context_complete = complete
    candidate = direct(run(dataset), "B")
    assert candidate["control_status"] == expected
    assert candidate["consequences"][0]["rules"][3]["status"] == expected
    assert candidate["consequences"][0]["rest_after"][0]["before_hours"] == 24 - previous_end + 8


def test_h4_missing_week6_context_then_confirmed_exact_11_hours(repository):
    dataset = repository.get_dataset("en-flytting")
    target = next(s for s in dataset.shifts if s.id == "X")
    target.start = dataset.week_end - timedelta(hours=10)
    target.end = dataset.week_end - timedelta(hours=2)
    dataset.coverage_end = dataset.week_end
    candidate = direct(run(dataset), "B")
    assert candidate["control_status"] == "uavklart"
    assert candidate["consequences"][0]["rules"][3]["status"] == "uavklart"
    assert candidate["consequences"][0]["rest_after"][0]["after_known"] is False
    following = Shift(
        id="week6-next",
        start=dataset.week_end + timedelta(hours=9),
        end=dataset.week_end + timedelta(hours=17),
        required_skill="K1",
        required_count=1,
    )
    dataset.coverage_end = dataset.week_end + timedelta(days=1)
    dataset.shifts.append(following)
    dataset.assignments.append(
        Assignment(id="next-B", employee_id="B", shift_id=following.id, locked=True)
    )
    candidate = direct(run(dataset), "B")
    assert candidate["control_status"] == "bestatt"
    assert candidate["consequences"][0]["rest_after"][0]["after_hours"] == 11


@pytest.mark.parametrize(
    "identifier,version,expected_x,expected_hours",
    [
        ("hovedscenario", "1.0", [], 32),
        ("oppdatert-plan", "2.1", ["A03"], 40),
    ],
)
def test_m1_m2_cumulative_absences_preserve_source_staffing(
    demo_client, identifier, version, expected_x, expected_hours
):
    base = {
        "dataset_id": identifier,
        "version": version,
        "absences": [{"employee_id": "A01", "shift_id": "X"}],
    }
    response = demo_client.post(
        "/api/absences/simulate",
        json={**base, "absence": {"employee_id": "A02", "shift_id": "W5-A02-3"}},
    )
    assert response.status_code == 200
    value = response.json()
    assert len(value["absences"]) == 2
    assert next(c for c in value["coverage"] if c["shift_id"] == "X")["assigned"] == expected_x
    assert next(c for c in value["coverage"] if c["shift_id"] == "W5-A02-3")["uncovered"] == 1
    result = demo_client.post(
        "/api/evaluate",
        json={
            **base,
            "absences": value["absences"],
            "target_shift_id": "W5-A02-3",
            "search_limit": 0,
            "criteria": ["P1"],
        },
    ).json()
    candidate = direct(result, "A03")
    assert Decimal(candidate["consequences"][0]["hours_before"]) == expected_hours
    if expected_hours == 40:
        assert candidate["consequences"][0]["rules"][-1]["status"] == "regelavvik"


def test_o4_new_version_recalculates_cost_from_new_rate(demo_client):
    old_body = {
        **body(),
        "absences": [
            {"employee_id": "A01", "shift_id": "X"},
            {"employee_id": "A02", "shift_id": "W5-A02-3"},
        ],
        "target_shift_id": "W5-A02-3",
    }
    old = demo_client.post("/api/evaluate", json=old_body).json()
    new = demo_client.post(
        "/api/evaluate", json={**old_body, "dataset_id": "oppdatert-plan", "version": "2.1"}
    ).json()
    assert direct(old, "A03")["cost"]["total"] == "1600.00"
    assert direct(new, "A03")["cost"]["total"] == "1800.00"
    assert direct(new, "A03")["cost"]["assignments"][0]["segments"][0]["rate"] == "225"
    assert direct(new, "A03")["id"] != direct(old, "A03")["id"]


@pytest.mark.parametrize("corruption", ["json", "reference"])
def test_503_unusable_dataset_never_leaks_filesystem(tmp_path, repository, corruption):
    path = tmp_path / "private-internal-path.json"
    if corruption == "json":
        path.write_text("{invalid", encoding="utf-8")
    else:
        dataset = repository.get_dataset("hovedscenario").model_dump(mode="json")
        dataset["assignments"][0]["employee_id"] = "does-not-exist"
        import json

        path.write_text(json.dumps(dataset), encoding="utf-8")
    client = TestClient(create_app(Settings(data_dir=tmp_path, _env_file=None)))
    response = client.get("/api/datasets/hovedscenario/state")
    assert response.status_code == 503
    assert "Datagrunnlaget kan ikke leses" in response.json()["message"]
    assert str(tmp_path) not in response.text
    assert path.name not in response.text


def test_duplicate_absences_keep_the_same_proposal_identity(repository):
    dataset = repository.get_dataset("hovedscenario")
    absence = Absence(employee_id="A01", shift_id="X")
    once = evaluate(dataset, [absence], "X", 0)
    twice = evaluate(dataset, [absence, absence], "X", 0)
    assert {a["id"] for a in once["alternatives"]} == {a["id"] for a in twice["alternatives"]}


def test_irrelevant_week1_collision_does_not_change_current_proposal(repository):
    dataset = repository.get_dataset("hovedscenario")
    old = next(s for s in dataset.shifts if s.id == "H1-A02")
    duplicate = old.model_copy(update={"id": "old-overlap"})
    dataset.shifts.append(duplicate)
    dataset.assignments.append(
        Assignment(id="old-overlap", employee_id="A02", shift_id=duplicate.id, locked=True)
    )
    proposal = direct(run(dataset), "A02")
    person = proposal["consequences"][0]
    assert proposal["control_status"] == "bestatt"
    assert person["rules"][2]["status"] == person["rules"][3]["status"] == "bestatt"
    assert (person["rest_after"][0]["before_hours"], person["rest_after"][0]["after_hours"]) == (
        16,
        16,
    )


def test_b_only_move_is_kept_when_y_stays_covered_and_c_also_qualifies(repository):
    dataset = repository.get_dataset("en-flytting")
    # F04 er en gyldig, låst opprinnelig tildeling på Y. C kan fortsatt supplere Y.
    employee = next(e for e in dataset.employees if e.id == "F04")
    employee.skills = ["K2"]
    employee.availability = [Interval(start=dataset.coverage_start, end=dataset.coverage_end)]
    dataset.assignments.append(Assignment(id="Y-F04", employee_id="F04", shift_id="Y", locked=True))
    result = run(dataset, 1)
    choices = [
        a
        for a in result["alternatives"]
        if a["candidate_id"] == "B" and a["moves"] == 1 and a["selectable"]
    ]
    alone = next(a for a in choices if a["affected_employee_ids"] == ["B"])
    replaced = next(a for a in choices if a["affected_employee_ids"] == ["B", "C"])
    assert next(p for p in alone["plan"] if p["shift_id"] == "Y")["after"] == ["F04"]
    assert next(p for p in replaced["plan"] if p["shift_id"] == "Y")["after"] == ["C", "F04"]
    assert alone["id"] != replaced["id"]


def test_short_coverage_never_reports_complete_zero_history(repository):
    dataset = repository.get_dataset("en-flytting")
    dataset.coverage_start = datetime.fromisoformat("2026-10-07T00:00:00+02:00")
    known = Shift(
        id="partial-history",
        start=datetime.fromisoformat("2026-10-08T08:00:00+02:00"),
        end=datetime.fromisoformat("2026-10-08T16:00:00+02:00"),
        required_skill="K1",
        required_count=1,
    )
    dataset.shifts.append(known)
    dataset.assignments.append(
        Assignment(id="partial-history", employee_id="B", shift_id=known.id, locked=True)
    )
    dataset = Dataset.model_validate(dataset.model_dump())
    weeks = history(dataset, "B")["weeks"]
    assert not any(w["complete"] for w in weeks)
    assert [w["known_hours"] for w in weeks] == [0, 0, 0, 8]
    assert weeks[3]["shift_ids"] == ["partial-history"]


def test_history_uses_oslo_calendar_boundaries_and_membership_across_dst(repository):
    dataset = repository.get_dataset("en-flytting")
    dataset.week_start = datetime.fromisoformat("2026-11-02T00:00:00+01:00")
    dataset.week_end = datetime.fromisoformat("2026-11-09T00:00:00+01:00")
    dataset.coverage_end = datetime.fromisoformat("2026-11-10T00:00:00+01:00")
    for sid, start, end in [
        ("local-midnight", "2026-10-19T00:00:00+02:00", "2026-10-19T01:00:00+02:00"),
        ("cross-midnight", "2026-10-25T23:30:00+01:00", "2026-10-26T00:30:00+01:00"),
    ]:
        dataset.shifts.append(
            Shift(
                id=sid,
                start=datetime.fromisoformat(start),
                end=datetime.fromisoformat(end),
                required_skill="K1",
                required_count=1,
            )
        )
        dataset.assignments.append(Assignment(id=sid, employee_id="B", shift_id=sid, locked=True))
    dataset = Dataset.model_validate(dataset.model_dump())
    weeks = history(dataset, "B")["weeks"]
    assert weeks[2]["start"].isoformat() == "2026-10-19T00:00:00+02:00"
    assert weeks[2]["end"].isoformat() == "2026-10-26T00:00:00+01:00"
    assert set(weeks[2]["shift_ids"]) == {"local-midnight", "cross-midnight"}
    assert weeks[2]["known_hours"] == Decimal("1.5")
    assert weeks[3]["shift_ids"] == ["cross-midnight"]
    assert weeks[3]["known_hours"] == Decimal("0.5")


def test_bundled_history_contract_and_incomplete_source_absent_variant(repository):
    dataset = repository.get_dataset("hovedscenario")
    candidate = direct(run(dataset), "A02")
    weeks = candidate["history"][0]["weeks"]
    source = next(e for e in dataset.employees if e.id == "A02").history_source
    assert len(weeks) == 4
    for index, week in enumerate(weeks, 1):
        assert week["known_hours"] == 8
        assert week["shift_ids"] == [f"H{index}-A02"]
        assert week["source"] == source
        assert week["complete"] is True
    assert weeks[0]["start"] == dataset.coverage_start
    assert weeks[-1]["end"] == dataset.week_start
    next(a for a in dataset.assignments if a.shift_id == "H1-A02").absent = True
    next(e for e in dataset.employees if e.id == "A02").history_complete = False
    incomplete = history(dataset, "A02")["weeks"]
    assert incomplete[0]["known_hours"] == 0 and incomplete[0]["shift_ids"] == []
    assert incomplete[1]["known_hours"] == 8
    assert all(not w["complete"] and w["source"] == source for w in incomplete)


def test_current_controls_membership_violation_and_absence_hours(tmp_path, repository):
    dataset = repository.get_dataset("hovedscenario")
    next(e for e in dataset.employees if e.id == "A05").availability = []
    (tmp_path / "demo.json").write_text(dataset.model_dump_json(), encoding="utf-8")
    client = TestClient(create_app(Settings(data_dir=tmp_path, _env_file=None)))
    initial = client.get("/api/datasets/hovedscenario/state").json()
    people = {p["employee_id"]: p for p in initial["current_controls"]}
    assert set(people) == {e.id for e in dataset.employees}
    assert people["A05"]["control_status"] == "regelavvik"
    assert people["A05"]["rules"][1]["status"] == "regelavvik"
    assert Decimal(people["A02"]["hours_after"]) == 24
    refreshed = client.post(
        "/api/state",
        json={
            "dataset_id": "hovedscenario",
            "version": "1.0",
            "absences": [
                {"employee_id": "A01", "shift_id": "X"},
                {"employee_id": "A01", "shift_id": "W5-A01-2"},
                {"employee_id": "A02", "shift_id": "W5-A02-3"},
            ],
        },
    ).json()
    people = {p["employee_id"]: p for p in refreshed["current_controls"]}
    assert set(people) == {e.id for e in dataset.employees} - {"A01"}
    assert Decimal(people["A02"]["hours_after"]) == 16
