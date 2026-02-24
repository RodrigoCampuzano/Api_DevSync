from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from src.application.dependencies import get_project_by_id
from src.application.schemas.project_schema import ProjectResponse
from src.domain.use_cases.projects.get_project_by_id import GetProjectByIdUseCase

router = APIRouter()


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(
    project_id: UUID,
    use_case: Annotated[GetProjectByIdUseCase, Depends(get_project_by_id)],
):
    """Get a project by ID."""
    project = await use_case.execute(project_id)
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return project
