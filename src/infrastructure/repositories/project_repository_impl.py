import uuid
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.project import Project
from src.domain.entities.project_member import ProjectMember
from src.domain.repositories.project_repository import ProjectRepository
from src.infrastructure.db.models import ProjectMemberModel, ProjectModel


def _to_project_entity(model: ProjectModel) -> Project:
    return Project(
        id=uuid.UUID(bytes=model.id),
        name=model.name,
        description=model.description,
        created_at=model.created_at,
    )


def _to_member_entity(model: ProjectMemberModel) -> ProjectMember:
    return ProjectMember(
        project_id=uuid.UUID(bytes=model.project_id),
        user_id=uuid.UUID(bytes=model.user_id),
        role=model.role,
        joined_at=model.joined_at,
    )


class ProjectRepositoryImpl(ProjectRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, project_id: UUID) -> Project | None:
        result = await self._session.execute(
            select(ProjectModel).where(ProjectModel.id == project_id.bytes)
        )
        model = result.scalar_one_or_none()
        return _to_project_entity(model) if model else None

    async def get_all(self) -> list[Project]:
        result = await self._session.execute(select(ProjectModel))
        return [_to_project_entity(m) for m in result.scalars().all()]

    async def create(self, project: Project) -> Project:
        model = ProjectModel(
            id=project.id.bytes,
            name=project.name,
            description=project.description,
            created_at=project.created_at,
        )
        self._session.add(model)
        await self._session.commit()
        await self._session.refresh(model)
        return _to_project_entity(model)

    async def add_member(self, member: ProjectMember) -> ProjectMember:
        model = ProjectMemberModel(
            project_id=member.project_id.bytes,
            user_id=member.user_id.bytes,
            role=member.role,
            joined_at=member.joined_at,
        )
        self._session.add(model)
        await self._session.commit()
        return _to_member_entity(model)

    async def get_members(self, project_id: UUID) -> list[ProjectMember]:
        result = await self._session.execute(
            select(ProjectMemberModel).where(
                ProjectMemberModel.project_id == project_id.bytes
            )
        )
        return [_to_member_entity(m) for m in result.scalars().all()]

    async def delete(self, project_id: UUID) -> bool:
        result = await self._session.execute(
            select(ProjectModel).where(ProjectModel.id == project_id.bytes)
        )
        model = result.scalar_one_or_none()
        if not model:
            return False
        await self._session.delete(model)
        await self._session.commit()
        return True

    async def update(self, project_id: UUID, name: str | None, description: str | None) -> Project:
        result = await self._session.execute(
            select(ProjectModel).where(ProjectModel.id == project_id.bytes)
        )
        model = result.scalar_one_or_none()
        if not model:
            from fastapi import HTTPException
            raise HTTPException(status_code=404, detail="Project not found")
        if name is not None:
            model.name = name
        if description is not None:
            model.description = description
        await self._session.commit()
        await self._session.refresh(model)
        return _to_project_entity(model)
