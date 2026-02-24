import uuid
from datetime import datetime
from uuid import UUID

from src.domain.entities.task import Task
from src.domain.repositories.task_repository import TaskRepository


class CreateTaskUseCase:
    def __init__(self, repository: TaskRepository):
        self._repo = repository

    async def execute(
        self,
        project_id: UUID,
        title: str,
        description: str | None,
        created_by: UUID,
    ) -> Task:
        task = Task(
            id=uuid.uuid4(),
            project_id=project_id,
            title=title,
            description=description,
            status="TODO",
            assigned_to=None,
            created_by=created_by,
            version=1,
            updated_at=datetime.utcnow(),
            created_at=datetime.utcnow(),
        )
        return await self._repo.create(task)
