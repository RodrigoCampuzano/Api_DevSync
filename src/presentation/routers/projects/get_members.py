from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from src.application.dependencies import get_project_members
from src.application.schemas.project_schema import MemberResponse
from src.domain.use_cases.projects.get_project_members import GetProjectMembersUseCase

router = APIRouter()


@router.get("/{project_id}/members", response_model=list[MemberResponse])
async def list_members(
    project_id: UUID,
    use_case: Annotated[GetProjectMembersUseCase, Depends(get_project_members)],
):
    """List all members of a project."""
    return await use_case.execute(project_id)
