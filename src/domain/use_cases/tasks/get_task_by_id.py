from uuid import UUID

from src.domain.entities.task import Task
from src.domain.repositories.task_repository import TaskRepository


class GetTaskByIdUseCase:
    def __init__(self, repository: TaskRepository):
        self._repo = repository

    async def execute(self, task_id: UUID) -> Task | None:
        return await self._repo.get_by_id(task_id)
