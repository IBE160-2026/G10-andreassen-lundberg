"""Standardtekster fra ferdige fakta. Funksjonene endrer aldri kontroll eller rang."""

from decimal import Decimal


def sorting_values(alternative):
    p1, p2 = alternative["p1"], alternative["p2"]
    hours = "uavklart timetall" if p1 is None else f"{p1} uketimer"
    share = (
        "uavklart andel av avtalte timer"
        if p2 is None
        else f"{Decimal(str(p2)) * 100:.1f} % av avtalte timer".replace(".", ",")
    )
    return f"P1: {hours}; P2: {share}"


def standard_explanation(alternative):
    candidate = alternative["candidate_id"]
    consequences = alternative["consequences"]
    main = next(c for c in consequences if c["employee_id"] == candidate)
    cost = alternative["cost"]
    affected_findings = [
        f"{person['employee_id']}: "
        + ", ".join(
            f"{rule['rule']} ({rule['status']})"
            for rule in person["rules"]
            if rule["status"] != "bestatt"
        )
        for person in consequences
        if person["control_status"] != "bestatt"
    ]
    return {
        "short_answer": f"Forslaget med {candidate} "
        + {
            "bestatt": "oppfyller scenarioreglene.",
            "regelavvik": "har regelavvik.",
            "uavklart": "har uavklart kontrollgrunnlag.",
        }[alternative["control_status"]]
        + (
            " Berørte kontroller: " + "; ".join(affected_findings) + "."
            if affected_findings
            else ""
        ),
        "tradeoff": f"{main['hours_before']} → {main['hours_after']} registrerte uketimer. "
        f"{alternative['moves']} flytting(er). P1/P2 gjelder hovedkandidaten. "
        + (
            f"Syntetisk kostnadsanslag: {cost['total']} NOK; differanse {cost['difference']} NOK."
            if cost["complete"]
            else "Kostnadsanslaget er uavklart."
        ),
        "consequences": "Berørte: "
        + ", ".join(alternative["affected_employee_ids"])
        + ". "
        + (
            "Forslaget dekker berørte vakter."
            if alternative["complete"]
            else "Udekket: " + ", ".join(c["shift_id"] for c in alternative["uncovered"])
        )
        + " Vaktlisten er uendret.",
        "uncertainty": " ".join(
            [m for c in consequences for m in c["missing"]]
            + cost["missing"]
            + alternative["sorting_missing"]
        )
        or "Avgrensede scenarioregler, ikke full kontroll av lov eller avtaler.",
    }


def explain_evaluation(result):
    return {
        **result,
        "alternatives": [
            {**alternative, "explanation": standard_explanation(alternative)}
            for alternative in result["alternatives"]
        ],
    }


def compare_explanation(alternative, reference, criteria):
    explanation = standard_explanation(alternative)
    if reference:
        explanation["tradeoff"] += (
            " Dette alternativet har øverste rang."
            if alternative["rank"] == 1
            else f" Øverst etter {' → '.join(criteria)} er {reference['candidate_id']}: "
            f"{sorting_values(reference)}. "
            f"Undersøkt alternativ: {sorting_values(alternative)}."
        )
    return explanation
