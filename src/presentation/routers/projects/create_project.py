from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.application.dependencies import get_create_project
from src.application.schemas.project_schema import ProjectCreate, ProjectResponse
from src.domain.use_cases.projects.create_project import CreateProjectUseCase

router = APIRouter()


@router.post("/", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
async def create_project(
    body: ProjectCreate,
    use_case: Annotated[CreateProjectUseCase, Depends(get_create_project)],
):
    """Create a new project (sprint board)."""
    return await use_case.execute(name=body.name, description=body.description)
