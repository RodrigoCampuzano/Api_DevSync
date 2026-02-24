from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.application.dependencies import get_authenticate_user
from src.application.schemas.user_schema import TokenResponse
from src.domain.use_cases.users.authenticate_user import AuthenticateUserUseCase

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    use_case: Annotated[AuthenticateUserUseCase, Depends(get_authenticate_user)],
):
    """
    Authenticate a user and return a JWT access token.
    Uses OAuth2PasswordRequestForm matching standard FastAPI docs behavior.
    """
    token = await use_case.execute(email=form_data.username, password=form_data.password)
    return {"access_token": token, "token_type": "bearer"}
