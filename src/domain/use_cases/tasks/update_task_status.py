from uuid import UUID

from src.domain.entities.task import Task
from src.domain.repositories.task_repository import TaskRepository


class UpdateTaskStatusUseCase:
    """
    Implements Optimistic Concurrency Control.
    The client sends the current `version` it knows about.
    If it doesn't match the DB, a ConflictError is raised.
    """

    def __init__(self, repository: TaskRepository):
        self._repo = repository

    async def execute(self, task_id: UUID, status: str, expected_version: int) -> Task:
        return await self._repo.update_status(task_id, status, expected_version)
