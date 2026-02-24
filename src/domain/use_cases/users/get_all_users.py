from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository


class GetAllUsersUseCase:
    def __init__(self, repository: UserRepository):
        self._repo = repository

    async def execute(self) -> list[User]:
        return await self._repo.get_all()
