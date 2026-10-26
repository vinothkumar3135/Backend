from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import auth, businesses, health
from app.core.config import settings
from app.database import models  # noqa: F401  (registers tables)
from app.database.session import Base as _Base, engine
from app.middleware.logging import RequestLogMiddleware
from app.utils.logging_setup import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    _Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)
app.add_middleware(RequestLogMiddleware)
app.include_router(health.router)
app.include_router(auth.router)
app.include_router(businesses.router)
