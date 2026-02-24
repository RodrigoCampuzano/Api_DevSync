from uuid import UUID

from src.domain.entities.project import Project
from src.domain.repositories.project_repository import ProjectRepository


class GetProjectByIdUseCase:
    def __init__(self, repository: ProjectRepository):
        self._repo = repository

    async def execute(self, project_id: UUID) -> Project | None:
        return await self._repo.get_by_id(project_id)
