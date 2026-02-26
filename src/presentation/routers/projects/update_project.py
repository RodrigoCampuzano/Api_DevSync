from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from src.application.dependencies import get_update_project
from src.application.schemas.project_schema import ProjectResponse, ProjectUpdate
from src.domain.use_cases.projects.update_project import UpdateProjectUseCase

router = APIRouter()


@router.put("/{project_id}", response_model=ProjectResponse)
async def update_project(
    project_id: UUID,
    body: ProjectUpdate,
    use_case: Annotated[UpdateProjectUseCase, Depends(get_update_project)],
):
    """Update a project's name and/or description."""
    project = await use_case.execute(
        project_id=project_id,
        name=body.name,
        description=body.description,
    )
    return project
