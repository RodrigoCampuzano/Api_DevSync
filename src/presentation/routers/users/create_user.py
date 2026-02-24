from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.application.dependencies import get_create_user
from src.application.schemas.user_schema import UserCreate, UserResponse
from src.domain.use_cases.users.create_user import CreateUserUseCase

router = APIRouter()


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    body: UserCreate,
    use_case: Annotated[CreateUserUseCase, Depends(get_create_user)],
):
    """Register a new user."""
    user = await use_case.execute(
        username=body.username,
        email=body.email,
        password=body.password,
    )
    return user
