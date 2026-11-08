from decimal import Decimal
from typing import Any, Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, model_validator

from ..data.schema import Absence, Dataset, DatasetInfo, Interval, Shift

Status = Literal["bestatt", "regelavvik", "uavklart"]


class Input(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Basis(Input):
    dataset_id: str
    version: str
    absences: list[Absence] = Field(default_factory=list)


class AbsenceRequest(Basis):
    absence: Absence


class AbsencePreviewRequest(Basis):
    employee_id: str
    start_shift_id: str
    calendar_days: int = Field(ge=1, strict=True)


class EvaluationRequest(Basis):
    target_shift_id: str
    search_limit: Literal[0, 1] = 1
    criteria: list[Literal["P1", "P2"]] = Field(default_factory=lambda: ["P1"])

    @model_validator(mode="after")
    def unique_criteria(self):
        if not self.criteria or len(set(self.criteria)) != len(self.criteria):
            raise ValueError("Velg minst ett kriterium, uten duplikater")
        return self


class ExplanationRequest(EvaluationRequest):
    alternative_id: str


class CompareRequest(Input):
    previous_id: str
    next_id: str


class CoverageResult(BaseModel):
    shift_id: str
    required: int
    assigned: list[str]
    uncovered: int


class RuleResult(BaseModel):
    rule: Literal["R1", "R2", "R3", "R4", "R5"]
    status: Literal["bestatt", "regelavvik", "uavklart", "ikke_vurdert"]
    value: str
    explanation: str
    source: str
    limitation: str


class RestResult(BaseModel):
    shift_id: str
    before_hours: Decimal | None
    after_hours: Decimal | None
    previous_shift_id: str | None
    next_shift_id: str | None
    before_known: bool
    after_known: bool
    collision: bool


class PersonResult(BaseModel):
    employee_id: str
    hours_before: Decimal
    hours_after: Decimal
    hours_complete: bool
    rest_before: list[RestResult]
    rest_after: list[RestResult]
    rules: list[RuleResult]
    control_status: Status
    missing: list[str]
    period_start: AwareDatetime
    period_end: AwareDatetime


class CostInterval(Interval):
    hours: Decimal
    rate: Decimal | None
    supplement: Decimal | None
    amount: Decimal | None


class AssignmentCost(BaseModel):
    employee_id: str
    shift_id: str
    segments: list[CostInterval]
    amount: Decimal | None
    missing: list[str]


class CostResult(BaseModel):
    currency: Literal["NOK"]
    complete: bool
    total: Decimal | None
    reference: Decimal | None
    difference: Decimal | None
    known_subtotal: Decimal
    assignments: list[AssignmentCost]
    reference_assignments: list[AssignmentCost]
    missing: list[str]
    omitted: list[str]


class HistoryWeek(Interval):
    week: int
    known_hours: Decimal
    shift_ids: list[str]
    source: str
    complete: bool
    limitation: str


class HistoryResult(BaseModel):
    employee_id: str
    weeks: list[HistoryWeek]


class ExplanationResult(BaseModel):
    short_answer: str
    tradeoff: str
    consequences: str
    uncertainty: str


class PlanChange(BaseModel):
    shift_id: str
    before: list[str]
    after: list[str]


class AlternativeResult(BaseModel):
    id: str
    candidate_id: str
    kind: Literal["direkte", "flytting", "delvis"]
    moves: int
    control_status: Status
    coverage_status: Literal["full", "delvis"]
    complete: bool
    selectable: bool
    affected_employee_ids: list[str]
    affected_shift_ids: list[str]
    plan: list[PlanChange]
    uncovered: list[CoverageResult]
    consequences: list[PersonResult]
    history: list[HistoryResult]
    cost: CostResult
    p1: Decimal | None
    p2: Decimal | None
    rank: int | None
    sorting_missing: list[str]
    explanation: ExplanationResult
    coverage_reason: str
    replacement_findings: list[dict]


class EvaluationResponse(EvaluationRequest):
    assessment_time: AwareDatetime
    search_status: Literal["fullfort", "avbrutt", "utenfor_omfang"]
    message: str
    coverage: list[CoverageResult]
    alternatives: list[AlternativeResult]
    combinations_examined: int
    duration_ms: float


class AbsenceResponse(Basis):
    coverage: list[CoverageResult]
    message: str


class PreviewShift(BaseModel):
    shift: Shift
    eligible: bool
    limitation: str


class PreviewResponse(Interval):
    affected: list[PreviewShift]


class DatasetChange(BaseModel):
    category: str
    id: str
    field: str
    before: Any
    after: Any
    label: str
    before_label: str
    after_label: str


class CompareResponse(BaseModel):
    previous: DatasetInfo
    next: DatasetInfo
    same_family: bool
    changes: list[DatasetChange]
    unchanged: bool


class ExplanationResponse(BaseModel):
    mode: Literal["standard"]
    message: str
    explanation: ExplanationResult
    reference_id: str | None


class StateResponse(Dataset):
    coverage: list[CoverageResult]
    current_controls: list[PersonResult]
