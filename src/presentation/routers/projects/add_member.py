from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, status

from src.application.dependencies import get_add_member
from src.application.schemas.project_schema import AddMemberRequest, MemberResponse
from src.domain.use_cases.projects.add_project_member import AddProjectMemberUseCase

router = APIRouter()


@router.post("/{project_id}/members", response_model=MemberResponse, status_code=status.HTTP_201_CREATED)
async def add_member(
    project_id: UUID,
    body: AddMemberRequest,
    use_case: Annotated[AddProjectMemberUseCase, Depends(get_add_member)],
):
    """Add a user to a project as ADMIN or DEVELOPER."""
    return await use_case.execute(
        project_id=project_id,
        user_id=body.user_id,
        role=body.role,
    )
