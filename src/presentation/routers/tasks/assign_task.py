from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from src.application.dependencies import get_assign_task
from src.application.schemas.task_schema import AssignTaskRequest, TaskResponse
from src.domain.use_cases.tasks.assign_task import AssignTaskUseCase

router = APIRouter()


@router.patch("/{task_id}/assign", response_model=TaskResponse)
async def assign_task(
    task_id: UUID,
    body: AssignTaskRequest,
    use_case: Annotated[AssignTaskUseCase, Depends(get_assign_task)],
):
    """Assign (or unassign) a task to a user."""
    task = await use_case.execute(task_id=task_id, user_id=body.user_id)
    return task
