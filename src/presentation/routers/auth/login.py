from typing import Annotated

from fastapi import APIRouter, Depends

from src.application.dependencies import get_authenticate_user
from src.application.schemas.user_schema import LoginRequest, TokenResponse
from src.domain.use_cases.users.authenticate_user import AuthenticateUserUseCase

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
async def login(
    body: LoginRequest,
    use_case: Annotated[AuthenticateUserUseCase, Depends(get_authenticate_user)],
):
    """
    Authenticate a user and return a JWT access token.
    Accepts a simple JSON body with `email` and `password`.
    """
    token = await use_case.execute(email=body.email, password=body.password)
    return {"access_token": token, "token_type": "bearer"}
