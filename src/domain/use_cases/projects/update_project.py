from uuid import UUID

from src.domain.entities.project import Project
from src.domain.repositories.project_repository import ProjectRepository


class UpdateProjectUseCase:
    def __init__(self, repository: ProjectRepository):
        self._repo = repository

    async def execute(
        self, project_id: UUID, name: str | None = None, description: str | None = None
    ) -> Project:
        return await self._repo.update(project_id, name=name, description=description)
