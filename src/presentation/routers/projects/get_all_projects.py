from typing import Annotated

from fastapi import APIRouter, Depends

from src.application.dependencies import get_all_projects
from src.application.schemas.project_schema import ProjectResponse
from src.domain.use_cases.projects.get_all_projects import GetAllProjectsUseCase

router = APIRouter()


@router.get("/", response_model=list[ProjectResponse])
async def list_projects(
    use_case: Annotated[GetAllProjectsUseCase, Depends(get_all_projects)],
):
    """List all projects."""
    return await use_case.execute()
