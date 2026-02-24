from src.domain.entities.project import Project
from src.domain.repositories.project_repository import ProjectRepository


class GetAllProjectsUseCase:
    def __init__(self, repository: ProjectRepository):
        self._repo = repository

    async def execute(self) -> list[Project]:
        return await self._repo.get_all()
