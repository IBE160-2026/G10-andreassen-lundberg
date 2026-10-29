from pydantic import BaseModel


class DatasetInfo(BaseModel):
    """Metadata som alle datasett har. Ansatte, vakter og behov kommer i SCRUM-19."""

    id: str
    version: str
    title: str
    description: str = ""
