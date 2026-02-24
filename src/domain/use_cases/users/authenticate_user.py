from fastapi import HTTPException

from src.domain.repositories.user_repository import UserRepository
from src.infrastructure.security.hashing import verify_password
from src.infrastructure.security.jwt import create_access_token


class AuthenticateUserUseCase:
    def __init__(self, repository: UserRepository):
        self._repo = repository

    async def execute(self, email: str, password: str) -> str:
        user = await self._repo.get_by_email(email)
        if not user:
            raise HTTPException(status_code=401, detail="Incorrect email or password")
        
        if not verify_password(password, user.password_hash):
            raise HTTPException(status_code=401, detail="Incorrect email or password")
        
        # Valid credentials, create token
        access_token = create_access_token(data={"sub": str(user.id)})
        return access_token
