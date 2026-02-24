from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.infrastructure.db.config import engine
from src.infrastructure.db.models import Base
from src.presentation.api_router import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create all tables if they don't exist yet (idempotent)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="DevSync API",
    description=(
        "Real-Time Sprint Board API.\n\n"
        "Manage users, projects, and tasks with Kanban-style status tracking. "
        "Supports **Optimistic Concurrency Control** on task updates and "
        "**real-time WebSocket broadcasts** per project room."
    ),
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/", tags=["Health"])
async def health_check():
    return {"status": "ok", "service": "DevSync API", "version": "1.0.0"}
