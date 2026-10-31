from pydantic import BaseModel, Field


class DatasetInfo(BaseModel):
    """Metadata som alle datasett har. Ansatte, vakter og behov kommer i SCRUM-19."""

    id: str = Field(pattern=r"^[A-Za-z0-9_-]+$")
    version: str
    title: str
    description: str = ""
