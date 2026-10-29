from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel

from .. import __version__
from ..data import DatasetInfo, DatasetNotFoundError, DatasetRepository
from ..explain import Explainer

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
