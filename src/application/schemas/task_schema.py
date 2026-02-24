from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import BaseModel

TaskStatus = Literal["TODO", "IN_PROGRESS", "REVIEW", "DONE"]
TaskRole = Literal["ADMIN", "DEVELOPER"]


class TaskCreate(BaseModel):
    project_id: UUID
    title: str
    description: str | None = None
    created_by: UUID


class TaskResponse(BaseModel):
    id: UUID
    project_id: UUID
    title: str
    description: str | None
    status: str
    assigned_to: UUID | None
    created_by: UUID
    version: int
    updated_at: datetime
    created_at: datetime

    model_config = {"from_attributes": True}


class UpdateTaskStatusRequest(BaseModel):
    status: TaskStatus
    version: int  # Required for Optimistic Concurrency Control


class AssignTaskRequest(BaseModel):
    user_id: UUID | None = None  # None = unassign
