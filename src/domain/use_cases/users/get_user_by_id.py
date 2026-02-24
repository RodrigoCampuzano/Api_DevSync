from uuid import UUID

from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository


class GetUserByIdUseCase:
    def __init__(self, repository: UserRepository):
        self._repo = repository

    async def execute(self, user_id: UUID) -> User | None:
        return await self._repo.get_by_id(user_id)
