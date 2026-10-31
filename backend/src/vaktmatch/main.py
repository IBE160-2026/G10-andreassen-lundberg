from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import __version__
from .api.routes import router
from .config import Settings, get_settings
from .data import DatasetRepository
from .explain import get_explainer


def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or get_settings()
    app = FastAPI(title="VaktMatch", version=__version__)
    app.state.repository = DatasetRepository(settings.data_dir)
    app.state.explainer = get_explainer(settings)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_methods=["GET", "POST"],
        allow_headers=["*"],
    )
    app.include_router(router)
    return app


app = create_app()
