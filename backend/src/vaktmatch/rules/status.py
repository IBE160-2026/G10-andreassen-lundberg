from enum import StrEnum


class ControlStatus(StrEnum):
    """Samlet kontrollstatus, jf. «Hva betyr resultatet?» i docs/forslag-ved-frafall.md."""

    PASSED = "bestatt"
    RULE_VIOLATION = "regelavvik"
    UNRESOLVED = "uavklart"
