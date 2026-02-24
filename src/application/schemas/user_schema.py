from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(..., max_length=72)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., max_length=72)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    id: UUID
    username: str
    email: str
    created_at: datetime

    model_config = {"from_attributes": True}
