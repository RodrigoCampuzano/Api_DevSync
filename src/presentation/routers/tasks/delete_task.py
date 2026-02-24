from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from src.application.dependencies import get_delete_task
from src.domain.use_cases.tasks.delete_task import DeleteTaskUseCase

router = APIRouter()


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: UUID,
    use_case: Annotated[DeleteTaskUseCase, Depends(get_delete_task)],
):
    """Delete a task by ID."""
    deleted = await use_case.execute(task_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
