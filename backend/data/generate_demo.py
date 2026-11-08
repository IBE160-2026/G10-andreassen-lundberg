"""Reproduserbare syntetiske data, skrevet av Codex på Odins mandat 08.11.2026.

Kjøres manuelt ved tilsiktet endring av de versjonerte JSON-filene, aldri av API.
Timene i hovedscenarioet følger docs/demoscenario-fravaer.md; historikk og
satser er nye konstruerte illustrasjoner. Ingen faktiske personer eller lønn.
"""

import json
from copy import deepcopy
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).parent / "datasets"


def stamp(day, hour=0):
    return f"2026-10-{day:02}T{hour:02}:00:00+02:00"


def base():
    data = {
        "dataset": {
            "id": "hovedscenario",
            "version": "1.0",
            "title": "To direkte alternativer",
            "family_id": "hoved",
            "description": (
                "S1: P1 gir A02 først, P2 gir A03 først. Syntetiske data av Codex på Odins mandat."
            ),
        },
        "assessment_time": stamp(14, 7),
        "week_start": stamp(12),
        "week_end": stamp(19),
        "coverage_start": "2026-09-14T00:00:00+02:00",
        "coverage_end": stamp(21),
        "employees": [],
        "shifts": [],
        "assignments": [],
        "supplements": [
            {"start": stamp(14, 8), "end": stamp(14, 16), "rate": "25", "shift_id": "X"}
        ],
    }
    for index, eid in enumerate([*(f"A{i:02}" for i in range(1, 9)), "V01"]):
        data["employees"].append(
            {
                "id": eid,
                "name": eid + " · eksempelperson",
                "kind": "external" if eid == "V01" else "internal",
                "skills": ["K2"] if eid == "A04" else ["K1"],
                "availability": None
                if eid == "V01"
                else [{"start": data["coverage_start"], "end": data["coverage_end"]}],
                "contract_hours": "24" if eid == "A02" else "40",
                "hourly_rate": "200" if eid == "A02" else str(180 + index * 10),
                "work_context_complete": True,
                "history_complete": True,
                "history_source": (
                    "Konstruerte registrerte vakter · Codex 08.11.2026, ikke faktisk utført arbeid"
                ),
            }
        )
        for week in range(4):
            start = datetime.fromisoformat(data["coverage_start"]) + timedelta(
                days=week * 7 + 1, hours=8
            )
            add(
                data,
                f"H{week + 1}-{eid}",
                eid,
                start.isoformat(),
                (start + timedelta(hours=8)).isoformat(),
                locked=True,
            )
    schedules = {
        "A01": [(14, 8, 14, 16), (16, 8, 16, 16)],
        "A02": [(12, 8, 12, 16), (13, 8, 13, 16), (15, 8, 15, 16)],
        "A03": [(12, 8, 12, 16), (13, 12, 13, 20), (15, 8, 15, 16), (16, 8, 16, 16)],
        "A04": [(12, 8, 12, 16), (13, 8, 13, 16), (15, 8, 15, 16)],
        "A05": [(12, 8, 12, 16), (13, 16, 14, 0), (15, 8, 15, 16)],
        "A06": [(12, 8, 12, 16), (13, 8, 13, 16), (14, 20, 15, 4)],
        "A07": [(13, 8, 13, 16), (14, 12, 14, 20), (15, 8, 15, 16)],
        "A08": [(day, 8, day, 16) for day in (12, 13, 15, 16, 17)],
        "V01": [(13, 8, 13, 16), (15, 8, 15, 16)],
    }
    for eid, slots in schedules.items():
        for index, (day, hour, end_day, end_hour) in enumerate(slots):
            sid = "X" if eid == "A01" and index == 0 else f"W5-{eid}-{index + 1}"
            add(data, sid, eid, stamp(day, hour), stamp(end_day, end_hour))
    # Uke-6-vakter gir konkret grensekontekst, og flyttes aldri av uke-5-søket.
    for eid in schedules:
        add(data, f"W6-{eid}", eid, stamp(19, 8), stamp(19, 16), locked=True)
    return data


def add(data, sid, eid, start, end, locked=False, skill="K1"):
    data["shifts"].append(
        {
            "id": sid,
            "start": start,
            "end": end,
            "required_skill": "K2" if eid == "A04" else skill,
            "required_count": 1,
        }
    )
    data["assignments"].append(
        {"id": "T-" + sid, "shift_id": sid, "employee_id": eid, "locked": locked, "absent": False}
    )


def save(data, identifier, title, version="1.0", family="hoved"):
    data["dataset"].update(id=identifier, title=title, version=version, family_id=family)
    data["dataset"]["description"] = (
        title + ". Syntetiske data konstruert av Codex på Odins mandat 08.11.2026."
    )
    (ROOT / (identifier + ".json")).write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def main():
    data = base()
    save(data, "hovedscenario", "To direkte alternativer")
    complete = deepcopy(data)
    complete["employees"][-1]["availability"] = [
        {"start": data["coverage_start"], "end": data["coverage_end"]}
    ]
    save(complete, "komplettert", "V01: tilgjengelighet bekreftet", "2.0")
    updated = deepcopy(data)
    updated["assignments"].append(
        {"id": "T-X-A03", "shift_id": "X", "employee_id": "A03", "locked": False, "absent": False}
    )
    updated["assignments"][
        next(i for i, a in enumerate(updated["assignments"]) if a["shift_id"] == "X")
    ]["absent"] = True
    updated["employees"][2]["hourly_rate"] = "225"
    save(updated, "oppdatert-plan", "Oppdatert plan: A03 dekker X", "2.1")
    save(deepcopy(data), "uendret", "Ny versjon, uendret innhold", "1.1")
    missing = deepcopy(data)
    for eid in ("A02", "A03"):
        employee = next(e for e in missing["employees"] if e["id"] == eid)
        employee["availability"] = [
            {"start": data["coverage_start"], "end": stamp(14, 8)},
            {"start": stamp(14, 16), "end": data["coverage_end"]},
        ]
    save(missing, "mangler", "S3: V01 mangler tilgjengelighet")
    missing_complete = deepcopy(missing)
    missing_complete["employees"][-1]["availability"] = complete["employees"][-1]["availability"]
    save(missing_complete, "mangler-komplettert", "S3: V01 komplettert", "2.0")
    unavailable = deepcopy(missing)
    unavailable["employees"][-1]["availability"] = []
    save(unavailable, "ingen-direkte", "S2: ingen direkte erstatter")
    p2missing = deepcopy(data)
    p2missing["employees"][2]["contract_hours"] = None
    save(p2missing, "mangler-p2", "S5: A03 mangler avtalte timer")
    tied = deepcopy(data)
    tied["assignments"] = [a for a in tied["assignments"] if a["shift_id"] != "W5-A03-4"]
    tied["shifts"] = [s for s in tied["shifts"] if s["id"] != "W5-A03-4"]
    tied["employees"][2]["contract_hours"] = "24"
    save(tied, "lik-rang", "S4: A02 og A03 har lik rang")
    movement = deepcopy(data)
    movement["employees"] = [deepcopy(data["employees"][i]) for i in (0, 1, 2)]
    for employee, eid in zip(movement["employees"], ["A", "B", "C"], strict=True):
        employee.update(
            id=eid, name=eid + " · eksempelperson", skills=["K1", "K2"], contract_hours="40"
        )
    movement["shifts"], movement["assignments"], movement["supplements"] = [], [], []
    add(movement, "X", "A", stamp(14, 8), stamp(14, 16))
    add(movement, "Y", "B", stamp(14, 12), stamp(14, 20))
    movement["shifts"][1]["required_skill"] = "K2"
    movement["employees"][2]["skills"] = ["K2"]
    movement["employees"][2]["availability"] = [{"start": stamp(14, 12), "end": stamp(14, 20)}]
    movement["supplements"] = [
        {"start": stamp(14, 8), "end": stamp(14, 16), "rate": "25", "shift_id": "X"}
    ]
    movement["employees"][1]["hourly_rate"] = "200"
    movement["employees"][2]["hourly_rate"] = "180"
    # Samme kandidatbredde som hoveddemoen. Disse har kjent utilgjengelighet
    # og K9, slik at F2 fortsatt isolerer B→X/C→Y uten ekstra løsninger.
    for eid in ["F04", "F05", "F06", "F07", "F08", "V01"]:
        employee = deepcopy(data["employees"][0])
        employee.update(
            id=eid,
            name=eid + " · eksempelperson",
            skills=["K9"],
            availability=[],
            kind="external" if eid == "V01" else "internal",
        )
        movement["employees"].append(employee)
    save(movement, "en-flytting", "Én flytting: B til X, C til Y", family="flytting")
    no_c = deepcopy(movement)
    no_c["employees"][2]["availability"] = []
    save(no_c, "udekket-y", "Én flytting uten erstatter på Y", family="flytting")


if __name__ == "__main__":
    main()
