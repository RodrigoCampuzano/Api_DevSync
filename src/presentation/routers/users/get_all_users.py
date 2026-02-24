from typing import Annotated

from fastapi import APIRouter, Depends

from src.application.dependencies import get_all_users
from src.application.schemas.user_schema import UserResponse
from src.domain.use_cases.users.get_all_users import GetAllUsersUseCase

router = APIRouter()


@router.get("/", response_model=list[UserResponse])
async def list_users(
    use_case: Annotated[GetAllUsersUseCase, Depends(get_all_users)],
):
    """List all users."""
    return await use_case.execute()
