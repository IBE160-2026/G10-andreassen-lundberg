"""Rene demoberegninger. Verken I/O, HTTP, modellkall eller planmutasjon."""

from datetime import timedelta
from decimal import ROUND_HALF_UP, Decimal
from hashlib import sha256
from itertools import combinations
from time import perf_counter
from zoneinfo import ZoneInfo

from ..data.schema import Absence, Assignment, Dataset, Employee, Interval, Shift, utc
from .status import ControlStatus

D = Decimal
RULE_SOURCE = "docs/demoscenario-fravaer.md · Odin 21.10.2026 · syntetiske data"
LIMITATIONS = {
    "R1": "Intern kompetansekode, ingen offentlig kvalifikasjonsstandard.",
    "R2": "Ledig kalender bekrefter ikke tilgjengelighet.",
    "R3": "Gjelder registrert arbeid og oppgitt fullstendighet.",
    "R4": "Forenklet 11-timersregel; ikke full lov- eller avtalekontroll.",
    "R5": "Høyst 40 timer i fast arbeidsuke; overtid og tariff er ikke modellert.",
}
OMITTED = [
    "Syntetiske satser og tillegg, ikke reelle lønnsavtaler.",
    "Overtid, tariff, sykefravær, arbeidsgiveravgift og full arbeidsgiverkostnad er utelatt.",
]


def hours(start, end) -> Decimal:
    delta = utc(end) - utc(start)
    return D(delta.days * 86400 + delta.seconds) / D(3600) + D(delta.microseconds) / D(
        3_600_000_000
    )


def overlap(a: Interval, b: Interval) -> bool:
    return utc(a.start) < utc(b.end) and utc(b.start) < utc(a.end)


def overlap_hours(a: Interval, b: Interval) -> Decimal:
    return max(D(0), hours(max(utc(a.start), utc(b.start)), min(utc(a.end), utc(b.end))))


def is_absent(assignment: Assignment, absences: list[Absence]) -> bool:
    return assignment.absent or any(
        a.employee_id == assignment.employee_id and a.shift_id == assignment.shift_id
        for a in absences
    )


def active_plan(dataset: Dataset, absences: list[Absence]) -> list[Assignment]:
    return [a for a in dataset.assignments if not is_absent(a, absences)]


def coverage(dataset: Dataset, plan: list[Assignment]) -> list[dict]:
    return [
        {
            "shift_id": shift.id,
            "required": shift.required_count,
            "assigned": sorted(a.employee_id for a in plan if a.shift_id == shift.id),
            "uncovered": max(
                0, shift.required_count - len([a for a in plan if a.shift_id == shift.id])
            ),
        }
        for shift in dataset.shifts
        if overlap(shift, Interval(start=dataset.week_start, end=dataset.week_end))
    ]


def week_hours(dataset: Dataset, employee_id: str, plan: list[Assignment]) -> Decimal:
    shifts = {s.id: s for s in dataset.shifts}
    week = Interval(start=dataset.week_start, end=dataset.week_end)
    return sum(
        (overlap_hours(shifts[a.shift_id], week) for a in plan if a.employee_id == employee_id),
        D(0),
    )


def aggregate(statuses) -> ControlStatus:
    if "regelavvik" in statuses:
        return ControlStatus.RULE_VIOLATION
    if "uavklart" in statuses or "ikke_vurdert" in statuses:
        return ControlStatus.UNRESOLVED
    return ControlStatus.PASSED


def available(employee: Employee, shift: Shift) -> bool | None:
    if employee.availability is None:
        return None
    cursor = utc(shift.start)
    for interval in sorted(employee.availability, key=lambda x: utc(x.start)):
        if utc(interval.start) > cursor:
            break
        if utc(interval.end) > cursor:
            cursor = utc(interval.end)
        if cursor >= utc(shift.end):
            return True
    return False


def rest_context(dataset: Dataset, employee: Employee, shift: Shift, plan: list[Assignment]):
    shifts = {s.id: s for s in dataset.shifts}
    others = [
        shifts[a.shift_id] for a in plan if a.employee_id == employee.id and a.shift_id != shift.id
    ]
    previous = max(
        (s for s in others if utc(s.end) <= utc(shift.start)),
        key=lambda s: utc(s.end),
        default=None,
    )
    following = min(
        (s for s in others if utc(s.start) >= utc(shift.end)),
        key=lambda s: utc(s.start),
        default=None,
    )
    before = hours(previous.end, shift.start) if previous else None
    after = hours(shift.end, following.start) if following else None
    before_known = employee.work_context_complete and (
        previous is not None or hours(dataset.coverage_start, shift.start) >= 11
    )
    after_known = employee.work_context_complete and (
        following is not None or hours(shift.end, dataset.coverage_end) >= 11
    )
    return {
        "shift_id": shift.id,
        "before_hours": before,
        "after_hours": after,
        "previous_shift_id": previous.id if previous else None,
        "next_shift_id": following.id if following else None,
        "before_known": before_known,
        "after_known": after_known,
        "collision": any(overlap(shift, s) for s in others),
    }


def control_person(dataset, employee, before, after, additions, absences):
    shifts = {s.id: s for s in dataset.shifts}
    new_shifts = [shifts[a.shift_id] for a in additions if a.employee_id == employee.id]
    checked_shifts = [
        shifts[a.shift_id]
        for a in after
        if a.employee_id == employee.id
        and overlap(shifts[a.shift_id], Interval(start=dataset.week_start, end=dataset.week_end))
    ]
    rules = []

    def row(code, checks, value, explanation):
        status = aggregate(checks)
        rules.append(
            {
                "rule": code,
                "status": status,
                "value": value,
                "explanation": explanation,
                "source": RULE_SOURCE,
                "limitation": LIMITATIONS[code],
            }
        )

    skills = [
        "uavklart"
        if employee.skills is None
        else ("bestatt" if s.required_skill in employee.skills else "regelavvik")
        for s in checked_shifts
    ]
    row(
        "R1",
        skills,
        ", ".join(f"{s.id}: {s.required_skill}" for s in checked_shifts),
        f"Kompetansegrunnlaget for {employee.id} mangler."
        if employee.skills is None
        else f"{employee.id} mangler nødvendig kompetanse for minst én vakt."
        if "regelavvik" in skills
        else "Kompetansekrav for alle berørtes tildelinger i sluttplanen er bekreftet.",
    )
    availability = []
    availability_details = []
    for shift in checked_shifts:
        absent = any(
            a.employee_id == employee.id and overlap(shifts[a.shift_id], shift) for a in absences
        ) or any(
            a.employee_id == employee.id and a.absent and overlap(shifts[a.shift_id], shift)
            for a in dataset.assignments
        )
        state = False if absent else available(employee, shift)
        availability.append("uavklart" if state is None else "bestatt" if state else "regelavvik")
        availability_details.append(
            f"{shift.id} ({shift.start.isoformat()}–{shift.end.isoformat()}): "
            + (
                "fravær"
                if absent
                else "ukjent"
                if state is None
                else "tilgjengelig"
                if state
                else "ikke tilgjengelig hele vakten"
            )
        )
    row(
        "R2",
        availability,
        "; ".join(availability_details),
        f"Tilgjengelighet for {employee.id} må avklares."
        if "uavklart" in availability
        else f"{employee.id} er ikke tilgjengelig hele den aktuelle vakten."
        if "regelavvik" in availability
        else "Bekreftet tilgjengelig hele tidsrommet.",
    )
    own = [shifts[a.shift_id] for a in after if a.employee_id == employee.id]
    week = Interval(start=dataset.week_start, end=dataset.week_end)
    relevant_ids = {s.id for s in checked_shifts + new_shifts}
    collision_pairs = [
        (a.id, b.id)
        for a, b in combinations(own, 2)
        if overlap(a, b)
        and (a.id in relevant_ids or b.id in relevant_ids or overlap(a, week) or overlap(b, week))
    ]
    row(
        "R3",
        [
            "regelavvik"
            if collision_pairs
            else "bestatt"
            if employee.work_context_complete
            else "uavklart"
        ],
        "; ".join(f"{a} / {b}" for a, b in collision_pairs) or "Ingen kjent overlapp",
        "Slutt lik start er ikke overlapp. Øvrig arbeid må være kjent.",
    )
    rests = [rest_context(dataset, employee, s, after) for s in new_shifts]
    # Kontroller også naboforhold i sluttplanen for alle berørte ansatte.
    relevant = [
        s for s in own if overlap(s, Interval(start=dataset.week_start, end=dataset.week_end))
    ]
    all_rests = [rest_context(dataset, employee, s, after) for s in relevant]
    violations = [
        r
        for r in all_rests
        if not r["collision"]
        and any(r[key] is not None and r[key] < 11 for key in ("before_hours", "after_hours"))
    ]
    missing_rest = any(not r["before_known"] or not r["after_known"] for r in all_rests)
    rest_status = "regelavvik" if violations else "uavklart" if missing_rest else "bestatt"
    rest_value = "; ".join(
        f"{r['shift_id']}: "
        f"{r['before_hours'] if r['before_hours'] is not None else 'ingen kjent nabovakt'}"
        f" / {r['after_hours'] if r['after_hours'] is not None else 'ingen kjent nabovakt'} t"
        for r in rests
    )
    if collision_pairs and not violations:
        rules.append(
            {
                "rule": "R4",
                "status": "ikke_vurdert",
                "value": rest_value,
                "explanation": "Hvile ikke vurdert ved kjent kollisjon.",
                "source": RULE_SOURCE,
                "limitation": LIMITATIONS["R4"],
            }
        )
    else:
        row("R4", [rest_status], rest_value, "Minst 11 timer på begge sider; uke 4 og 6 inngår.")
    total = week_hours(dataset, employee.id, after)
    row(
        "R5",
        [
            "regelavvik"
            if total > 40
            else "bestatt"
            if employee.work_context_complete
            else "uavklart"
        ],
        str(total),
        "Høyst 40 timer. Bare faktisk periodeoverlapp teller, beregnet fra vaktene.",
    )
    return {
        "employee_id": employee.id,
        "hours_before": week_hours(dataset, employee.id, before),
        "hours_after": total,
        "hours_complete": employee.work_context_complete,
        "rest_before": [rest_context(dataset, employee, s, before) for s in new_shifts],
        "rest_after": rests,
        "rules": rules,
        "control_status": aggregate([r["status"] for r in rules]),
        "missing": [r["explanation"] for r in rules if r["status"] == "uavklart"],
        "period_start": dataset.week_start,
        "period_end": dataset.week_end,
    }


def cost_assignment(dataset: Dataset, assignment: Assignment) -> dict:
    shift = next(s for s in dataset.shifts if s.id == assignment.shift_id)
    employee = next(e for e in dataset.employees if e.id == assignment.employee_id)
    missing = []
    if employee.hourly_rate is None:
        missing.append(f"Timesats mangler for {employee.id}.")
    if dataset.supplements is None:
        missing.append("Tilleggsgrunnlag mangler.")
    applicable = [
        s
        for s in dataset.supplements or []
        if (s.employee_id is None or s.employee_id == employee.id)
        and (s.shift_id is None or s.shift_id == shift.id)
        and overlap(s, shift)
    ]
    boundaries = sorted(
        {
            utc(shift.start),
            utc(shift.end),
            *(max(utc(shift.start), utc(s.start)) for s in applicable),
            *(min(utc(shift.end), utc(s.end)) for s in applicable),
        }
    )
    segments = []
    subtotal = D(0)
    for start, end in zip(boundaries, boundaries[1:], strict=False):
        supplement = sum(
            (s.rate for s in applicable if utc(s.start) <= start and utc(s.end) >= end), D(0)
        )
        amount = hours(start, end) * (employee.hourly_rate + supplement) if not missing else None
        subtotal += amount or D(0)
        segments.append(
            {
                "start": start,
                "end": end,
                "hours": hours(start, end),
                "rate": employee.hourly_rate,
                "supplement": supplement if dataset.supplements is not None else None,
                "amount": amount,
            }
        )
    return {
        "employee_id": employee.id,
        "shift_id": shift.id,
        "segments": segments,
        "amount": None if missing else subtotal.quantize(D("0.01"), rounding=ROUND_HALF_UP),
        "missing": missing,
    }


def cost(dataset, before, after, affected_shifts):
    original = [cost_assignment(dataset, a) for a in before if a.shift_id in affected_shifts]
    proposal = [cost_assignment(dataset, a) for a in after if a.shift_id in affected_shifts]
    missing = sorted({m for a in original + proposal for m in a["missing"]})
    reference = sum((a["amount"] or D(0) for a in original), D(0))
    total = sum((a["amount"] or D(0) for a in proposal), D(0))
    return {
        "currency": "NOK",
        "complete": not missing,
        "total": None if missing else total,
        "reference": None if missing else reference,
        "difference": None if missing else total - reference,
        "known_subtotal": total,
        "assignments": proposal,
        "reference_assignments": original,
        "missing": missing,
        "omitted": OMITTED,
    }


def history(dataset, employee_id):
    employee = next(e for e in dataset.employees if e.id == employee_id)
    shifts = {s.id: s for s in dataset.shifts}
    results = []
    for index in range(4):
        start = dataset.week_start.astimezone(ZoneInfo("Europe/Oslo")) - timedelta(weeks=4 - index)
        end = start + timedelta(weeks=1)
        interval = Interval(start=start, end=end)
        worked = [
            shifts[a.shift_id]
            for a in dataset.assignments
            if a.employee_id == employee_id
            and not a.absent
            and overlap(shifts[a.shift_id], interval)
        ]
        results.append(
            {
                "week": index + 1,
                "start": start,
                "end": end,
                "known_hours": sum((overlap_hours(s, interval) for s in worked), D(0)),
                "shift_ids": [s.id for s in worked],
                "source": employee.history_source,
                "complete": (
                    employee.history_complete
                    and utc(dataset.coverage_start) <= utc(start)
                    and utc(dataset.coverage_end) >= utc(end)
                ),
                "limitation": "Registrerte vakter dokumenterer ikke alene faktisk utført arbeid.",
            }
        )
    return {"employee_id": employee_id, "weeks": results}


def build_alternative(dataset, absences, before, target_id, candidate, removed, additions):
    after = [a for a in before if a.id not in {r.id for r in removed}] + additions
    affected_shifts = sorted({target_id, *(a.shift_id for a in removed + additions)})
    people = sorted({a.employee_id for a in additions + removed})
    employees = {e.id: e for e in dataset.employees}
    consequences = [
        control_person(dataset, employees[p], before, after, additions, absences) for p in people
    ]
    before_coverage = coverage(dataset, before)
    after_coverage = coverage(dataset, after)
    uncovered = [c for c in after_coverage if c["shift_id"] in affected_shifts and c["uncovered"]]
    complete = not uncovered
    status = aggregate([c["control_status"] for c in consequences])
    main = next(c for c in consequences if c["employee_id"] == candidate)
    contract = employees[candidate].contract_hours
    identity = repr(
        (
            dataset.dataset.id,
            dataset.dataset.version,
            sorted({(a.employee_id, a.shift_id) for a in absences}),
            target_id,
            sorted((a.employee_id, a.shift_id) for a in after),
        )
    )
    alternative_id = sha256(identity.encode()).hexdigest()[:20]
    result = {
        "id": alternative_id,
        "candidate_id": candidate,
        "kind": "direkte" if not removed else "flytting" if complete else "delvis",
        "moves": len(removed),
        "control_status": status,
        "coverage_status": "full" if complete else "delvis",
        "complete": complete,
        "selectable": complete and status == ControlStatus.PASSED,
        "affected_employee_ids": people,
        "affected_shift_ids": affected_shifts,
        "plan": [
            {
                "shift_id": sid,
                "before": next(c["assigned"] for c in before_coverage if c["shift_id"] == sid),
                "after": next(c["assigned"] for c in after_coverage if c["shift_id"] == sid),
            }
            for sid in affected_shifts
        ],
        "uncovered": uncovered,
        "consequences": consequences,
        "history": [history(dataset, p) for p in people],
        "cost": cost(dataset, before, after, affected_shifts),
        "p1": main["hours_after"] if main["hours_complete"] else None,
        "p2": main["hours_after"] / contract if contract and main["hours_complete"] else None,
        "rank": None,
        "sorting_missing": [],
        "coverage_reason": "",
        "replacement_findings": [],
    }
    return result


def rank_alternatives(alternatives, criteria):
    ranked = []
    for alternative in alternatives:
        alternative["rank"] = None
        alternative["sorting_missing"] = [
            f"{c}: nødvendig timetall mangler" for c in criteria if alternative[c.lower()] is None
        ]
        if alternative["selectable"] and not alternative["sorting_missing"]:
            ranked.append(alternative)

    def key(a):
        return tuple(a[c.lower()] for c in criteria)

    ranked.sort(key=lambda a: (key(a), a["id"]))
    previous, rank = None, 0
    for index, alternative in enumerate(ranked):
        values = key(alternative)
        if values != previous:
            rank = index + 1
        alternative["rank"] = rank
        previous = values
    return sorted(
        alternatives,
        key=lambda a: (
            a["rank"] is None,
            a["rank"] or 0,
            not a["selectable"],
            a["candidate_id"],
            a["id"],
        ),
    )


def evaluate(
    dataset: Dataset,
    absences: list[Absence],
    target_shift_id: str,
    search_limit: int = 1,
    criteria: list[str] | None = None,
) -> dict:
    started = perf_counter()
    criteria = criteria or ["P1"]
    before = active_plan(dataset, absences)
    current = coverage(dataset, before)
    target = next(s for s in dataset.shifts if s.id == target_shift_id)
    missing = next((c["uncovered"] for c in current if c["shift_id"] == target.id), None)
    response = {
        "dataset_id": dataset.dataset.id,
        "version": dataset.dataset.version,
        "absences": absences,
        "assessment_time": dataset.assessment_time,
        "target_shift_id": target.id,
        "search_limit": search_limit,
        "criteria": criteria,
        "search_status": "fullfort",
        "message": "Søket er fullført innenfor valgt søkeomfang.",
        "coverage": current,
        "alternatives": [],
        "combinations_examined": 0,
        "duration_ms": 0.0,
    }
    if (
        utc(target.start) <= utc(dataset.assessment_time)
        or utc(target.start) < utc(dataset.week_start)
        or utc(target.start) >= utc(dataset.week_end)
        or missing != 1
    ):
        response.update(
            search_status="utenfor_omfang",
            message=(
                "Ikke kjørt – utenfor omfang. Velg en framtidig uke-5-vakt med én udekket plass."
            ),
        )
        return response
    alternatives = []
    for employee in dataset.employees:
        if any(a.employee_id == employee.id and a.shift_id == target.id for a in before):
            continue
        addition = Assignment(
            id=f"proposal-{employee.id}-{target.id}", employee_id=employee.id, shift_id=target.id
        )
        alternatives.append(
            build_alternative(dataset, absences, before, target.id, employee.id, [], [addition])
        )
    if search_limit == 1:
        shifts = {s.id: s for s in dataset.shifts}
        employees = {e.id: e for e in dataset.employees}
        for assignment in before:
            shift = shifts[assignment.shift_id]
            if (
                assignment.locked
                or assignment.shift_id == target.id
                or employees[assignment.employee_id].kind != "internal"
                or utc(shift.start) <= utc(dataset.assessment_time)
                or utc(shift.start) < utc(dataset.week_start)
                or utc(shift.start) >= utc(dataset.week_end)
                or any(
                    a.employee_id == assignment.employee_id and a.shift_id == target.id
                    for a in before
                )
            ):
                continue
            addition = Assignment(
                id=f"proposal-{assignment.employee_id}-{target.id}",
                employee_id=assignment.employee_id,
                shift_id=target.id,
            )
            complete_found = False
            replacement_findings = []
            for employee in dataset.employees:
                if employee.id == assignment.employee_id or any(
                    a.employee_id == employee.id and a.shift_id == shift.id for a in before
                ):
                    continue
                replacement = Assignment(
                    id=f"proposal-{employee.id}-{shift.id}",
                    employee_id=employee.id,
                    shift_id=shift.id,
                )
                alternative = build_alternative(
                    dataset,
                    absences,
                    before,
                    target.id,
                    assignment.employee_id,
                    [assignment],
                    [addition, replacement],
                )
                complete_found |= alternative["selectable"]
                alternatives.append(alternative)
                replacement_control = next(
                    c for c in alternative["consequences"] if c["employee_id"] == employee.id
                )
                replacement_findings.append(
                    {
                        "employee_id": employee.id,
                        "control_status": replacement_control["control_status"],
                        "findings": [
                            f"{r['rule']}: {r['status']} · {r['value']}. {r['explanation']}"
                            for r in replacement_control["rules"]
                            if r["status"] != "bestatt"
                        ],
                    }
                )
            partial = build_alternative(
                dataset,
                absences,
                before,
                target.id,
                assignment.employee_id,
                [assignment],
                [addition],
            )
            if partial["complete"] or not complete_found:
                partial["coverage_reason"] = (
                    ""
                    if partial["complete"]
                    else (
                        f"Ingen komplett, bestått kombinasjon bekrefter dekning av {shift.id}. "
                        "Se de konkrete erstatningskontrollene; "
                        "kjent brudd har forrang for mangler."
                    )
                )
                partial["replacement_findings"] = replacement_findings
                alternatives.append(partial)
    response["combinations_examined"] = len(alternatives)
    alternatives = list({a["id"]: a for a in alternatives}.values())
    response["alternatives"] = rank_alternatives(alternatives, criteria)
    if not any(a["selectable"] for a in alternatives):
        response["message"] = "Ingen kontrollerte alternativer funnet innenfor valgt søkeomfang."
    response["duration_ms"] = round((perf_counter() - started) * 1000, 3)
    return response
