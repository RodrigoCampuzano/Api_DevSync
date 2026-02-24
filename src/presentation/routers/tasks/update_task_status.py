from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from src.application.dependencies import get_update_task_status
from src.application.schemas.task_schema import TaskResponse, UpdateTaskStatusRequest
from src.domain.use_cases.tasks.update_task_status import UpdateTaskStatusUseCase

router = APIRouter()


@router.patch("/{task_id}/status", response_model=TaskResponse)
async def update_task_status(
    task_id: UUID,
    body: UpdateTaskStatusRequest,
    use_case: Annotated[UpdateTaskStatusUseCase, Depends(get_update_task_status)],
):
    """
    Update a task's Kanban status.

    Implements **Optimistic Concurrency Control**: you must supply the current
    `version` of the task. If the server version differs, a **409 Conflict**
    is returned so the client can rollback its optimistic UI update.

    On success the version is auto-incremented.
    """
    task = await use_case.execute(
        task_id=task_id,
        status=body.status,
        expected_version=body.version,
    )
    return task
