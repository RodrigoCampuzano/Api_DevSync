from uuid import UUID

from src.domain.entities.task import Task
from src.domain.repositories.task_repository import TaskRepository


class GetTasksByProjectUseCase:
    def __init__(self, repository: TaskRepository):
        self._repo = repository

    async def execute(self, project_id: UUID) -> list[Task]:
        return await self._repo.get_by_project(project_id)
