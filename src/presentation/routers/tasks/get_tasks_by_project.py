from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from src.application.dependencies import get_tasks_by_project
from src.application.schemas.task_schema import TaskResponse
from src.domain.use_cases.tasks.get_tasks_by_project import GetTasksByProjectUseCase

router = APIRouter()


@router.get("/project/{project_id}", response_model=list[TaskResponse])
async def get_tasks_by_project(
    project_id: UUID,
    use_case: Annotated[GetTasksByProjectUseCase, Depends(get_tasks_by_project)],
):
    """Get all tasks for a specific project (Kanban board data)."""
    return await use_case.execute(project_id)
