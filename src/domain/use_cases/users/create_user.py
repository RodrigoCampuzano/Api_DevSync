import uuid
from datetime import datetime

from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository
from src.infrastructure.security.hashing import get_password_hash


class CreateUserUseCase:
    def __init__(self, repository: UserRepository):
        self._repo = repository

    async def execute(self, username: str, email: str, password: str) -> User:
        hashed = get_password_hash(password)
        user = User(
            id=uuid.uuid4(),
            username=username,
            email=email,
            password_hash=hashed,
            created_at=datetime.utcnow(),
        )
        return await self._repo.create(user)
