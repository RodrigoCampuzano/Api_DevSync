from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr


class UserResponse(BaseModel):
    id: UUID
    username: str
    email: str
    created_at: datetime

    model_config = {"from_attributes": True}
