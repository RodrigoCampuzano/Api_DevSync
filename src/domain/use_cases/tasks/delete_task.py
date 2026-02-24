from uuid import UUID

from src.domain.repositories.task_repository import TaskRepository


class DeleteTaskUseCase:
    def __init__(self, repository: TaskRepository):
        self._repo = repository

    async def execute(self, task_id: UUID) -> bool:
        return await self._repo.delete(task_id)
