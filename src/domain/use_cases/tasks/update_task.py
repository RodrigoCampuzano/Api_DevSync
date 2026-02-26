from uuid import UUID

from src.domain.entities.task import Task
from src.domain.repositories.task_repository import TaskRepository


class UpdateTaskUseCase:
    def __init__(self, repository: TaskRepository):
        self._repo = repository

    async def execute(
        self,
        task_id: UUID,
        expected_version: int,
        title: str | None = None,
        description: str | None = None,
        status: str | None = None,
        assigned_to: UUID | None = None,
    ) -> Task:
        return await self._repo.update(
            task_id=task_id,
            expected_version=expected_version,
            title=title,
            description=description,
            status=status,
            assigned_to=assigned_to,
        )
