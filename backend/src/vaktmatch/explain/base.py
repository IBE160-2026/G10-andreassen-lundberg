from typing import Protocol

from pydantic import BaseModel

from ..rules import ControlStatus


class Explanation(BaseModel):
    """Fast svarformat. Feltene utvides i SCRUM-39."""

    source: str
    summary: str


class Explainer(Protocol):
    name: str

    def explain(self, status: ControlStatus) -> Explanation: ...
