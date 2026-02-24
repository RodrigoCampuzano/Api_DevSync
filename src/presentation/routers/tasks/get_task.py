from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from src.application.dependencies import get_task_by_id
from src.application.schemas.task_schema import TaskResponse
from src.domain.use_cases.tasks.get_task_by_id import GetTaskByIdUseCase

router = APIRouter()


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: UUID,
    use_case: Annotated[GetTaskByIdUseCase, Depends(get_task_by_id)],
):
    """Get a single task by ID."""
    task = await use_case.execute(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task
