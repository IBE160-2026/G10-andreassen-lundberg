from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from . import __version__
from .api.routes import router
from .config import Settings, get_settings
from .data import DatasetLoadError, DatasetNotFoundError, DatasetRepository
from .explain import get_explainer


def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or get_settings()
    app = FastAPI(title="VaktMatch", version=__version__)
    app.state.repository = DatasetRepository(settings.data_dir)
    app.state.explainer = get_explainer(settings)

    @app.exception_handler(DatasetNotFoundError)
    async def not_found(request: Request, error: DatasetNotFoundError):
        return JSONResponse(status_code=404, content={"message": "Datasettet finnes ikke."})

    @app.exception_handler(DatasetLoadError)
    async def invalid_data(request: Request, error: DatasetLoadError):
        return JSONResponse(
            status_code=503,
            content={
                "message": "Datagrunnlaget kan ikke leses. Velg et annet datasett eller prøv igjen."
            },
        )

    @app.exception_handler(HTTPException)
    async def http_error(request: Request, error: HTTPException):
        return JSONResponse(status_code=error.status_code, content={"message": str(error.detail)})

    @app.exception_handler(RequestValidationError)
    async def input_error(request: Request, error: RequestValidationError):
        return JSONResponse(
            status_code=422,
            content={
                "message": "Kontroller feltene og prøv igjen.",
                "fields": [
                    {
                        "field": ".".join(str(p) for p in e["loc"][1:]),
                        "message": "Ugyldig eller manglende verdi.",
                    }
                    for e in error.errors()
                ],
            },
        )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_methods=["GET", "POST"],
        allow_headers=["*"],
    )
    app.include_router(router)
    return app


app = create_app()
