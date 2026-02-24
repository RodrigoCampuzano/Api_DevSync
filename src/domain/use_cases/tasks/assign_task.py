from uuid import UUID

from src.domain.entities.task import Task
from src.domain.repositories.task_repository import TaskRepository


class AssignTaskUseCase:
    def __init__(self, repository: TaskRepository):
        self._repo = repository

    async def execute(self, task_id: UUID, user_id: UUID | None) -> Task:
        return await self._repo.assign(task_id, user_id)
