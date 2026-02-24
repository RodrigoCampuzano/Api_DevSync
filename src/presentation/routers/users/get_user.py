from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from src.application.dependencies import get_user_by_id
from src.application.schemas.user_schema import UserResponse
from src.domain.use_cases.users.get_user_by_id import GetUserByIdUseCase

router = APIRouter()


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: UUID,
    use_case: Annotated[GetUserByIdUseCase, Depends(get_user_by_id)],
):
    """Get a user by ID."""
    user = await use_case.execute(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
