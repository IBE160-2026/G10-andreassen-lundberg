from datetime import UTC, datetime, timedelta
from decimal import Decimal
from typing import Literal
from zoneinfo import ZoneInfo

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, model_validator


class DatasetInfo(BaseModel):
    """Versjonert, offentlig identifikasjon av et syntetisk datasett."""

    id: str = Field(pattern=r"^[A-Za-z0-9_-]+$")
    version: str
    title: str
    description: str = ""
    family_id: str = ""


class DataModel(BaseModel):
    model_config = ConfigDict(extra="forbid", allow_inf_nan=False)


def utc(value: datetime) -> datetime:
    return value.astimezone(UTC)


class Interval(DataModel):
    start: AwareDatetime
    end: AwareDatetime

    @model_validator(mode="after")
    def ordered(self):
        if utc(self.start) >= utc(self.end):
            raise ValueError("Start må være før slutt")
        return self


class Employee(DataModel):
    id: str = Field(min_length=1)
    name: str
    kind: Literal["internal", "external"] = "internal"
    skills: list[str] | None
    availability: list[Interval] | None
    contract_hours: Decimal | None = Field(default=None, ge=0)
    hourly_rate: Decimal | None = Field(default=None, ge=0)
    work_context_complete: bool
    history_complete: bool
    history_source: str


class Shift(Interval):
    id: str = Field(min_length=1)
    required_skill: str
    required_count: int = Field(gt=0, strict=True)


class Assignment(DataModel):
    id: str = Field(min_length=1)
    employee_id: str
    shift_id: str
    locked: bool = False
    absent: bool = False


class Supplement(Interval):
    rate: Decimal = Field(ge=0)
    employee_id: str | None = None
    shift_id: str | None = None


class Absence(DataModel):
    employee_id: str
    shift_id: str


class Dataset(DataModel):
    dataset: DatasetInfo
    assessment_time: AwareDatetime
    week_start: AwareDatetime
    week_end: AwareDatetime
    coverage_start: AwareDatetime
    coverage_end: AwareDatetime
    employees: list[Employee]
    shifts: list[Shift]
    assignments: list[Assignment]
    supplements: list[Supplement] | None

    @model_validator(mode="after")
    def references(self):
        employees = {e.id for e in self.employees}
        shifts = {s.id for s in self.shifts}
        for items in (self.employees, self.shifts, self.assignments):
            if len({item.id for item in items}) != len(items):
                raise ValueError("ID-er må være unike innen hver objekttype")
        pairs = set()
        for assignment in self.assignments:
            if assignment.employee_id not in employees or assignment.shift_id not in shifts:
                raise ValueError("Tildelingen har ukjent ansatt eller vakt")
            pair = (assignment.employee_id, assignment.shift_id)
            if pair in pairs:
                raise ValueError("Samme ansatt kan ikke ha to tildelinger på samme vakt")
            pairs.add(pair)
        for supplement in self.supplements or []:
            if supplement.employee_id is not None and supplement.employee_id not in employees:
                raise ValueError("Tillegget har ukjent ansatt")
            if supplement.shift_id is not None and supplement.shift_id not in shifts:
                raise ValueError("Tillegget har ukjent vakt")
        if (
            not utc(self.coverage_start)
            <= utc(self.week_start)
            < utc(self.week_end)
            <= utc(self.coverage_end)
        ):
            raise ValueError("Kontrollperioden må omslutte arbeidsuken")
        oslo = ZoneInfo("Europe/Oslo")
        local_start = self.week_start.astimezone(oslo)
        local_end = self.week_end.astimezone(oslo)
        if local_end != local_start + timedelta(days=7):
            raise ValueError("Arbeidsuken må dekke sju kalenderdager")
        for shift in self.shifts:
            if utc(shift.start) < utc(self.coverage_start) or utc(shift.end) > utc(
                self.coverage_end
            ):
                raise ValueError("Vakten ligger utenfor bekreftet kontrollperiode")
        return self
