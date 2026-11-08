from datetime import datetime, timedelta
from typing import Annotated
from zoneinfo import ZoneInfo

from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel

from .. import __version__
from ..data import DatasetInfo, DatasetNotFoundError, DatasetRepository
from ..data.schema import Dataset, utc
from ..explain import Explainer
from ..explain.demoflow import compare_explanation, explain_evaluation
from ..rules.engine import active_plan, control_person, coverage, evaluate
from .models import (
    AbsencePreviewRequest,
    AbsenceRequest,
    AbsenceResponse,
    Basis,
    CompareRequest,
    CompareResponse,
    EvaluationRequest,
    EvaluationResponse,
    ExplanationRequest,
    ExplanationResponse,
    PreviewResponse,
    StateResponse,
)
from .presentation import readable_change
from .serialization import exact

router = APIRouter(prefix="/api")


def get_repository(request: Request) -> DatasetRepository:
    return request.app.state.repository


def get_explainer_dep(request: Request) -> Explainer:
    return request.app.state.explainer


Repository = Annotated[DatasetRepository, Depends(get_repository)]
ExplainerDep = Annotated[Explainer, Depends(get_explainer_dep)]


class Health(BaseModel):
    status: str
    version: str
    explainer: str


@router.get("/health")
def health(explainer: ExplainerDep) -> Health:
    return Health(status="ok", version=__version__, explainer=explainer.name)


@router.get("/datasets")
def list_datasets(repository: Repository) -> list[DatasetInfo]:
    return repository.list_datasets()


@router.get("/datasets/{dataset_id}")
def get_dataset(dataset_id: str, repository: Repository) -> DatasetInfo:
    try:
        return repository.get_info(dataset_id)
    except DatasetNotFoundError:
        raise HTTPException(status_code=404, detail="Datasettet finnes ikke") from None


def load_basis(body: Basis, repository: DatasetRepository) -> Dataset:
    dataset = repository.get_dataset(body.dataset_id)
    if body.version != dataset.dataset.version:
        raise HTTPException(
            409, "Dataversjonen er utdatert. Last inn gjeldende data og vurder på nytt."
        )
    for absence in body.absences:
        if not any(
            a.employee_id == absence.employee_id and a.shift_id == absence.shift_id
            for a in dataset.assignments
        ):
            raise HTTPException(
                422, "Et tidligere fravær viser til en ukjent ansatt eller tildeling."
            )
        shift = next(s for s in dataset.shifts if s.id == absence.shift_id)
        source_absence = any(
            a.employee_id == absence.employee_id and a.shift_id == absence.shift_id and a.absent
            for a in dataset.assignments
        )
        if (
            utc(shift.start) < utc(dataset.week_start)
            or utc(shift.start) >= utc(dataset.week_end)
            or (utc(shift.start) <= utc(dataset.assessment_time) and not source_absence)
        ):
            raise HTTPException(
                422,
                (
                    "Fraværsgrunnlaget må gjelde framtidige uke-5-vakter "
                    "eller kildeført fravær i uke 5."
                ),
            )
    return dataset


def state(dataset, absences):
    plan = active_plan(dataset, absences)
    weekly = {
        s.id
        for s in dataset.shifts
        if utc(s.start) < utc(dataset.week_end) and utc(s.end) > utc(dataset.week_start)
    }
    return {
        **dataset.model_dump(),
        "coverage": coverage(dataset, plan),
        "current_controls": [
            control_person(
                dataset,
                e,
                plan,
                plan,
                [a for a in plan if a.employee_id == e.id and a.shift_id in weekly],
                absences,
            )
            for e in dataset.employees
            if any(a.employee_id == e.id and a.shift_id in weekly for a in plan)
        ],
    }


@router.get("/datasets/{dataset_id}/state", response_model=StateResponse)
def get_state(dataset_id: str, repository: Repository):
    return state(repository.get_dataset(dataset_id), [])


@router.post("/state", response_model=StateResponse)
def refresh_state(body: Basis, repository: Repository):
    return state(load_basis(body, repository), body.absences)


@router.post("/absences/simulate", response_model=AbsenceResponse)
def simulate_absence(body: AbsenceRequest, repository: Repository) -> dict:
    dataset = load_basis(body, repository)
    absence = body.absence
    assignment = next(
        (
            a
            for a in dataset.assignments
            if a.employee_id == absence.employee_id and a.shift_id == absence.shift_id
        ),
        None,
    )
    if assignment is None:
        raise HTTPException(422, "Velg en ansatt og en vakt vedkommende er tildelt.")
    shift = next(s for s in dataset.shifts if s.id == absence.shift_id)
    if (
        utc(shift.start) <= utc(dataset.assessment_time)
        or utc(shift.start) < utc(dataset.week_start)
        or utc(shift.start) >= utc(dataset.week_end)
    ):
        raise HTTPException(
            422, "Velg en framtidig vakt helt innenfor uke 5. Påbegynte vakter kan ikke velges."
        )
    duplicate = absence in body.absences or assignment.absent
    absences = list(body.absences)
    if absence not in absences:
        absences.append(absence)
    absences = sorted(set((a.employee_id, a.shift_id) for a in absences))
    from ..data.schema import Absence

    active_absences = [Absence(employee_id=eid, shift_id=sid) for eid, sid in absences]
    return {
        "dataset_id": dataset.dataset.id,
        "version": dataset.dataset.version,
        "absences": active_absences,
        "coverage": coverage(dataset, active_plan(dataset, active_absences)),
        "message": "Fravær er allerede simulert for denne vakten."
        if duplicate
        else "Fraværet er simulert for valgt vakt. Finn alternativer når du er klar.",
    }


@router.post("/absences/preview", response_model=PreviewResponse)
def preview_absence(body: AbsencePreviewRequest, repository: Repository) -> dict:
    dataset = load_basis(body, repository)
    if not any(e.id == body.employee_id for e in dataset.employees):
        raise HTTPException(422, "Velg en kjent ansatt.")
    assigned = {a.shift_id for a in dataset.assignments if a.employee_id == body.employee_id}
    shift = next(
        (s for s in dataset.shifts if s.id == body.start_shift_id and s.id in assigned), None
    )
    if shift is None:
        raise HTTPException(422, "Velg en startvakt for denne ansatte.")
    oslo = ZoneInfo("Europe/Oslo")
    start = datetime.combine(shift.start.astimezone(oslo).date(), datetime.min.time(), oslo)
    try:
        end = start + timedelta(days=body.calendar_days)
    except (OverflowError, ValueError):
        raise HTTPException(422, "Perioden er for lang til en gyldig kalenderdato.") from None
    affected = []
    for item in sorted(dataset.shifts, key=lambda s: utc(s.start)):
        if item.id not in assigned or utc(item.start) >= utc(end) or utc(item.end) <= utc(start):
            continue
        eligible = utc(item.start) > utc(dataset.assessment_time) and utc(
            dataset.week_start
        ) <= utc(item.start) < utc(dataset.week_end)
        affected.append(
            {
                "shift": item,
                "eligible": eligible,
                "limitation": "" if eligible else "Påbegynt eller utenfor uke 5; kan ikke velges.",
            }
        )
    return {"start": start, "end": end, "affected": affected}


def run_evaluation(body, repository):
    dataset = load_basis(body, repository)
    if not any(s.id == body.target_shift_id for s in dataset.shifts):
        raise HTTPException(422, "Målskiftet finnes ikke i dette datasettet.")
    return explain_evaluation(
        evaluate(dataset, body.absences, body.target_shift_id, body.search_limit, body.criteria)
    )


@router.post("/evaluate", response_model=EvaluationResponse)
def evaluate_request(body: EvaluationRequest, repository: Repository) -> dict:
    return exact(run_evaluation(body, repository))


@router.post("/explain", response_model=ExplanationResponse)
def explain_request(body: ExplanationRequest, repository: Repository) -> dict:
    result = run_evaluation(body, repository)
    alternative = next((a for a in result["alternatives"] if a["id"] == body.alternative_id), None)
    if alternative is None:
        raise HTTPException(422, "Alternativet finnes ikke på dette grunnlaget. Kjør ny vurdering.")
    reference = next((a for a in result["alternatives"] if a["rank"] == 1), None)
    explanation = compare_explanation(alternative, reference, body.criteria)
    return exact(
        {
            "mode": "standard",
            "message": "KI-forklaring er ikke tilgjengelig. Standardforklaringen vises fortsatt.",
            "explanation": explanation,
            "reference_id": reference["id"] if reference else None,
        }
    )


@router.post("/datasets/compare", response_model=CompareResponse)
def compare_datasets(body: CompareRequest, repository: Repository) -> dict:
    previous = repository.get_dataset(body.previous_id)
    following = repository.get_dataset(body.next_id)
    changes = []
    for field in (
        "assessment_time",
        "week_start",
        "week_end",
        "coverage_start",
        "coverage_end",
        "supplements",
    ):
        old, new = getattr(previous, field), getattr(following, field)
        if old != new:
            changes.append(
                {"category": field, "id": field, "field": field, "before": old, "after": new}
            )
    for category in ("employees", "shifts", "assignments"):
        old = {item.id: item.model_dump() for item in getattr(previous, category)}
        new = {item.id: item.model_dump() for item in getattr(following, category)}
        for identifier in sorted(old.keys() | new.keys()):
            if identifier not in old or identifier not in new:
                changes.append(
                    {
                        "category": category,
                        "id": identifier,
                        "field": "objekt",
                        "before": old.get(identifier),
                        "after": new.get(identifier),
                    }
                )
            else:
                for field in old[identifier]:
                    if old[identifier][field] != new[identifier][field]:
                        changes.append(
                            {
                                "category": category,
                                "id": identifier,
                                "field": field,
                                "before": old[identifier][field],
                                "after": new[identifier][field],
                            }
                        )
    return exact(
        {
            "previous": previous.dataset,
            "next": following.dataset,
            "same_family": previous.dataset.family_id == following.dataset.family_id,
            "changes": [readable_change(change) for change in changes],
            "unchanged": not changes,
        }
    )
