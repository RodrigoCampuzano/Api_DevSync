from uuid import UUID

from src.domain.repositories.user_repository import UserRepository


class DeleteUserUseCase:
    def __init__(self, repository: UserRepository):
        self._repo = repository

    async def execute(self, user_id: UUID) -> bool:
        return await self._repo.delete(user_id)
