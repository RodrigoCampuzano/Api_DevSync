from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from src.application.dependencies import get_delete_project
from src.domain.use_cases.projects.delete_project import DeleteProjectUseCase

router = APIRouter()


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(
    project_id: UUID,
    use_case: Annotated[DeleteProjectUseCase, Depends(get_delete_project)],
):
    """Delete a project and all its tasks (CASCADE)."""
    deleted = await use_case.execute(project_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
