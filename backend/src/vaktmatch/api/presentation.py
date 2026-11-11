"""Lesbare datadifferanser. Ingen regelberegning eller nye produktvurderinger."""

from datetime import datetime
from decimal import Decimal
from zoneinfo import ZoneInfo

from pydantic import BaseModel

CATEGORY_NAMES = {
    "employees": "Ansatte",
    "shifts": "Vakter",
    "assignments": "Tildelinger",
    "supplements": "Timetillegg",
    "assessment_time": "Vurderingstidspunkt",
    "week_start": "Arbeidsukens start",
    "week_end": "Arbeidsukens slutt",
    "coverage_start": "Kontrollperiodens start",
    "coverage_end": "Kontrollperiodens slutt",
}
FIELD_NAMES = {
    "objekt": "Hele oppføringen",
    "id": "ID",
    "name": "Navn",
    "kind": "Tilknytning",
    "skills": "Kompetanse",
    "availability": "Tilgjengelighet",
    "contract_hours": "Avtalte uketimer",
    "hourly_rate": "Syntetisk timesats",
    "work_context_complete": "Fullstendig arbeidsgrunnlag",
    "history_complete": "Fullstendig historikk",
    "history_source": "Historikkens kilde",
    "start": "Start",
    "end": "Slutt",
    "required_skill": "Kompetansebehov",
    "required_count": "Bemanningsbehov",
    "employee_id": "Ansatt",
    "shift_id": "Vakt",
    "locked": "Lås",
    "absent": "Kildeført fravær",
    "rate": "Syntetisk timetillegg",
}


def display_value(field, value):
    if value is None:
        return "Mangler opplysninger / ingen oppføring"
    if isinstance(value, BaseModel):
        value = value.model_dump()
    if isinstance(value, datetime):
        return value.astimezone(ZoneInfo("Europe/Oslo")).strftime("%d.%m.%Y kl. %H.%M")
    if isinstance(value, bool):
        if field == "locked":
            return "Låst" if value else "Ulåst"
        return "Ja" if value else "Nei"
    if isinstance(value, (int, Decimal)):
        return str(value).replace(".", ",") + (
            " kr/time"
            if field in ("rate", "hourly_rate")
            else " t"
            if field == "contract_hours"
            else ""
        )
    if isinstance(value, list):
        if not value:
            return {"availability": "Kjent utilgjengelig", "supplements": "Ingen timetillegg"}.get(
                field, "Ingen oppføringer"
            )
        return "; ".join(display_value(field, item) for item in value)
    if isinstance(value, dict):
        return "; ".join(
            f"{FIELD_NAMES.get(key, CATEGORY_NAMES.get(key, key))}: {display_value(key, item)}"
            for key, item in value.items()
        )
    return {"internal": "Intern", "external": "Ekstern"}.get(str(value), str(value))


def readable_change(change):
    field_name = FIELD_NAMES.get(
        change["field"], CATEGORY_NAMES.get(change["field"], change["field"])
    )
    return {
        **change,
        "label": f"{CATEGORY_NAMES.get(change['category'], change['category'])} · "
        f"{change['id']} · {field_name}",
        "before_label": display_value(change["field"], change["before"]),
        "after_label": display_value(change["field"], change["after"]),
    }
