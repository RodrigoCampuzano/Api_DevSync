from uuid import UUID

from src.domain.repositories.project_repository import ProjectRepository


class DeleteProjectUseCase:
    def __init__(self, repository: ProjectRepository):
        self._repo = repository

    async def execute(self, project_id: UUID) -> bool:
        return await self._repo.delete(project_id)
