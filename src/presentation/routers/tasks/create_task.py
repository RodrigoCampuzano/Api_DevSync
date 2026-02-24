from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.application.dependencies import get_create_task
from src.application.schemas.task_schema import TaskCreate, TaskResponse
from src.domain.use_cases.tasks.create_task import CreateTaskUseCase

router = APIRouter()


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    body: TaskCreate,
    use_case: Annotated[CreateTaskUseCase, Depends(get_create_task)],
):
    """Create a new task (ticket) in TODO status."""
    return await use_case.execute(
        project_id=body.project_id,
        title=body.title,
        description=body.description,
        created_by=body.created_by,
    )
