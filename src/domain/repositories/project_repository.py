from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.entities.project import Project
from src.domain.entities.project_member import ProjectMember


class ProjectRepository(ABC):

    @abstractmethod
    async def get_by_id(self, project_id: UUID) -> Project | None:
        ...

    @abstractmethod
    async def get_all(self) -> list[Project]:
        ...

    @abstractmethod
    async def create(self, project: Project) -> Project:
        ...

    @abstractmethod
    async def add_member(self, member: ProjectMember) -> ProjectMember:
        ...

    @abstractmethod
    async def get_members(self, project_id: UUID) -> list[ProjectMember]:
        ...

    @abstractmethod
    async def delete(self, project_id: UUID) -> bool:
        ...
