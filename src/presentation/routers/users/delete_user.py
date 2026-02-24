from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from src.application.dependencies import get_delete_user
from src.domain.use_cases.users.delete_user import DeleteUserUseCase

router = APIRouter()


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: UUID,
    use_case: Annotated[DeleteUserUseCase, Depends(get_delete_user)],
):
    """Delete a user by ID."""
    deleted = await use_case.execute(user_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
