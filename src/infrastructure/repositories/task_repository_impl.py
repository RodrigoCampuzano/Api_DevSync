import uuid
from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.task import Task
from src.domain.repositories.task_repository import TaskRepository
from src.infrastructure.db.models import TaskModel


def _to_entity(model: TaskModel) -> Task:
    return Task(
        id=uuid.UUID(bytes=model.id),
        project_id=uuid.UUID(bytes=model.project_id),
        title=model.title,
        description=model.description,
        status=model.status,
        assigned_to=uuid.UUID(bytes=model.assigned_to) if model.assigned_to else None,
        created_by=uuid.UUID(bytes=model.created_by),
        version=model.version,
        updated_at=model.updated_at,
        created_at=model.created_at,
    )


class TaskRepositoryImpl(TaskRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, task_id: UUID) -> Task | None:
        result = await self._session.execute(
            select(TaskModel).where(TaskModel.id == task_id.bytes)
        )
        model = result.scalar_one_or_none()
        return _to_entity(model) if model else None

    async def get_by_project(self, project_id: UUID) -> list[Task]:
        result = await self._session.execute(
            select(TaskModel).where(TaskModel.project_id == project_id.bytes)
        )
        return [_to_entity(m) for m in result.scalars().all()]

    async def create(self, task: Task) -> Task:
        model = TaskModel(
            id=task.id.bytes,
            project_id=task.project_id.bytes,
            title=task.title,
            description=task.description,
            status=task.status,
            assigned_to=task.assigned_to.bytes if task.assigned_to else None,
            created_by=task.created_by.bytes,
            version=task.version,
        )
        self._session.add(model)
        await self._session.commit()
        await self._session.refresh(model)
        return _to_entity(model)

    async def update_status(self, task_id: UUID, status: str, expected_version: int) -> Task:
        """
        Optimistic Concurrency Control:
        Only updates if the current version matches expected_version.
        Raises HTTP 409 if another client already changed the task.
        """
        result = await self._session.execute(
            select(TaskModel).where(TaskModel.id == task_id.bytes)
        )
        model = result.scalar_one_or_none()
        if not model:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

        if model.version != expected_version:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    f"Version conflict: expected version {expected_version} "
                    f"but current version is {model.version}. "
                    "Please refresh and retry."
                ),
            )

        model.status = status
        model.version = model.version + 1
        await self._session.commit()
        await self._session.refresh(model)
        return _to_entity(model)

    async def assign(self, task_id: UUID, user_id: UUID | None) -> Task:
        result = await self._session.execute(
            select(TaskModel).where(TaskModel.id == task_id.bytes)
        )
        model = result.scalar_one_or_none()
        if not model:
            raise HTTPException(status_code=404, detail="Task not found")
        model.assigned_to = user_id.bytes if user_id else None
        await self._session.commit()
        await self._session.refresh(model)
        return _to_entity(model)

    async def delete(self, task_id: UUID) -> bool:
        result = await self._session.execute(
            select(TaskModel).where(TaskModel.id == task_id.bytes)
        )
        model = result.scalar_one_or_none()
        if not model:
            return False
        await self._session.delete(model)
        await self._session.commit()
        return True

    async def update(
        self,
        task_id: UUID,
        expected_version: int,
        title: str | None = None,
        description: str | None = None,
        status: str | None = None,
        assigned_to: UUID | None = None,
    ) -> Task:
        result = await self._session.execute(
            select(TaskModel).where(TaskModel.id == task_id.bytes)
        )
        model = result.scalar_one_or_none()
        if not model:
            raise HTTPException(status_code=404, detail="Task not found")

        if model.version != expected_version:
            raise HTTPException(
                status_code=409,
                detail=(
                    f"Version conflict: expected {expected_version} "
                    f"but current is {model.version}. Refresh and retry."
                ),
            )

        if title is not None:
            model.title = title
        if description is not None:
            model.description = description
        if status is not None:
            model.status = status
        if assigned_to is not None:
            model.assigned_to = assigned_to.bytes
        model.version = model.version + 1
        await self._session.commit()
        await self._session.refresh(model)
        return _to_entity(model)
