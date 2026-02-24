import uuid
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository
from src.infrastructure.db.models import UserModel


def _to_entity(model: UserModel) -> User:
    return User(
        id=uuid.UUID(bytes=model.id),
        username=model.username,
        email=model.email,
        created_at=model.created_at,
    )


class UserRepositoryImpl(UserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, user_id: UUID) -> User | None:
        result = await self._session.execute(
            select(UserModel).where(UserModel.id == user_id.bytes)
        )
        model = result.scalar_one_or_none()
        return _to_entity(model) if model else None

    async def get_by_email(self, email: str) -> User | None:
        result = await self._session.execute(
            select(UserModel).where(UserModel.email == email)
        )
        model = result.scalar_one_or_none()
        return _to_entity(model) if model else None

    async def get_all(self) -> list[User]:
        result = await self._session.execute(select(UserModel))
        return [_to_entity(m) for m in result.scalars().all()]

    async def create(self, user: User) -> User:
        model = UserModel(
            id=user.id.bytes,
            username=user.username,
            email=user.email,
            created_at=user.created_at,
        )
        self._session.add(model)
        await self._session.commit()
        await self._session.refresh(model)
        return _to_entity(model)

    async def delete(self, user_id: UUID) -> bool:
        result = await self._session.execute(
            select(UserModel).where(UserModel.id == user_id.bytes)
        )
        model = result.scalar_one_or_none()
        if not model:
            return False
        await self._session.delete(model)
        await self._session.commit()
        return True
