import uuid
from datetime import datetime

from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository


class CreateUserUseCase:
    def __init__(self, repository: UserRepository):
        self._repo = repository

    async def execute(self, username: str, email: str) -> User:
        user = User(
            id=uuid.uuid4(),
            username=username,
            email=email,
            created_at=datetime.utcnow(),
        )
        return await self._repo.create(user)
