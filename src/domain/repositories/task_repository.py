from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.entities.task import Task


class TaskRepository(ABC):

    @abstractmethod
    async def get_by_id(self, task_id: UUID) -> Task | None:
        ...

    @abstractmethod
    async def get_by_project(self, project_id: UUID) -> list[Task]:
        ...

    @abstractmethod
    async def create(self, task: Task) -> Task:
        ...

    @abstractmethod
    async def update_status(self, task_id: UUID, status: str, expected_version: int) -> Task:
        """Raises ConflictError if version mismatch (Optimistic Concurrency Control)."""
        ...

    @abstractmethod
    async def assign(self, task_id: UUID, user_id: UUID | None) -> Task:
        ...

    @abstractmethod
    async def delete(self, task_id: UUID) -> bool:
        ...
