from datetime import datetime
from uuid import UUID

from src.domain.entities.project_member import ProjectMember
from src.domain.repositories.project_repository import ProjectRepository


class AddProjectMemberUseCase:
    def __init__(self, repository: ProjectRepository):
        self._repo = repository

    async def execute(self, project_id: UUID, user_id: UUID, role: str = "DEVELOPER") -> ProjectMember:
        member = ProjectMember(
            project_id=project_id,
            user_id=user_id,
            role=role,
            joined_at=datetime.utcnow(),
        )
        return await self._repo.add_member(member)
