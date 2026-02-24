import uuid
from datetime import datetime

from src.domain.entities.project import Project
from src.domain.repositories.project_repository import ProjectRepository


class CreateProjectUseCase:
    def __init__(self, repository: ProjectRepository):
        self._repo = repository

    async def execute(self, name: str, description: str | None) -> Project:
        project = Project(
            id=uuid.uuid4(),
            name=name,
            description=description,
            created_at=datetime.utcnow(),
        )
        return await self._repo.create(project)
