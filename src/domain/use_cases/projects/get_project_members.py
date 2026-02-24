from uuid import UUID

from src.domain.entities.project_member import ProjectMember
from src.domain.repositories.project_repository import ProjectRepository


class GetProjectMembersUseCase:
    def __init__(self, repository: ProjectRepository):
        self._repo = repository

    async def execute(self, project_id: UUID) -> list[ProjectMember]:
        return await self._repo.get_members(project_id)
