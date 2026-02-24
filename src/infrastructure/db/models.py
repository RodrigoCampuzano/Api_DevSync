import uuid

from sqlalchemy import (
    BINARY, Column, Enum, ForeignKey, Index, Integer, String, Text, TIMESTAMP
)
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.sql import func


def generate_uuid_bytes() -> bytes:
    return uuid.uuid4().bytes


class Base(DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__ = "users"

    id = Column(BINARY(16), primary_key=True, default=generate_uuid_bytes)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    memberships = relationship("ProjectMemberModel", back_populates="user", cascade="all, delete")
    tasks_assigned = relationship("TaskModel", foreign_keys="TaskModel.assigned_to", back_populates="assignee")
    tasks_created = relationship("TaskModel", foreign_keys="TaskModel.created_by", back_populates="creator")


class ProjectModel(Base):
    __tablename__ = "projects"

    id = Column(BINARY(16), primary_key=True, default=generate_uuid_bytes)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

    members = relationship("ProjectMemberModel", back_populates="project", cascade="all, delete")
    tasks = relationship("TaskModel", back_populates="project", cascade="all, delete")


class ProjectMemberModel(Base):
    __tablename__ = "project_members"

    project_id = Column(BINARY(16), ForeignKey("projects.id", ondelete="CASCADE"), primary_key=True)
    user_id = Column(BINARY(16), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    role = Column(Enum("ADMIN", "DEVELOPER"), default="DEVELOPER")
    joined_at = Column(TIMESTAMP, server_default=func.now())

    project = relationship("ProjectModel", back_populates="members")
    user = relationship("UserModel", back_populates="memberships")


class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(BINARY(16), primary_key=True, default=generate_uuid_bytes)
    project_id = Column(BINARY(16), ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(Enum("TODO", "IN_PROGRESS", "REVIEW", "DONE"), default="TODO")
    assigned_to = Column(BINARY(16), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_by = Column(BINARY(16), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    version = Column(Integer, default=1, nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    created_at = Column(TIMESTAMP, server_default=func.now())

    project = relationship("ProjectModel", back_populates="tasks")
    assignee = relationship("UserModel", foreign_keys=[assigned_to], back_populates="tasks_assigned")
    creator = relationship("UserModel", foreign_keys=[created_by], back_populates="tasks_created")

    __table_args__ = (
        Index("idx_project_status", "project_id", "status"),
    )
