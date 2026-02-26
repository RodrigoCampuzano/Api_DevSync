from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from src.application.dependencies import get_update_task
from src.application.schemas.task_schema import TaskResponse, TaskUpdate
from src.domain.use_cases.tasks.update_task import UpdateTaskUseCase

router = APIRouter()


@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: UUID,
    body: TaskUpdate,
    use_case: Annotated[UpdateTaskUseCase, Depends(get_update_task)],
):
    """
    Update a task. Requires `version` for optimistic concurrency control.
    Returns 409 Conflict if version mismatch.
    """
    task = await use_case.execute(
        task_id=task_id,
        expected_version=body.version,
        title=body.title,
        description=body.description,
        status=body.status,
        assigned_to=body.assigned_to,
    )
    return task
