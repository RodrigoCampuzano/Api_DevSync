from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.db.config import get_db
from src.infrastructure.repositories.project_repository_impl import ProjectRepositoryImpl
from src.infrastructure.repositories.task_repository_impl import TaskRepositoryImpl
from src.infrastructure.repositories.user_repository_impl import UserRepositoryImpl

# ── Use Cases: Users ──────────────────────────────────────────────────────────
from src.domain.use_cases.users.create_user import CreateUserUseCase
from src.domain.use_cases.users.get_user_by_id import GetUserByIdUseCase
from src.domain.use_cases.users.get_all_users import GetAllUsersUseCase
from src.domain.use_cases.users.delete_user import DeleteUserUseCase
from src.domain.use_cases.users.authenticate_user import AuthenticateUserUseCase

# ── Use Cases: Projects ───────────────────────────────────────────────────────
from src.domain.use_cases.projects.create_project import CreateProjectUseCase
from src.domain.use_cases.projects.get_project_by_id import GetProjectByIdUseCase
from src.domain.use_cases.projects.get_all_projects import GetAllProjectsUseCase
from src.domain.use_cases.projects.add_project_member import AddProjectMemberUseCase
from src.domain.use_cases.projects.get_project_members import GetProjectMembersUseCase
from src.domain.use_cases.projects.delete_project import DeleteProjectUseCase

# ── Use Cases: Tasks ──────────────────────────────────────────────────────────
from src.domain.use_cases.tasks.create_task import CreateTaskUseCase
from src.domain.use_cases.tasks.get_task_by_id import GetTaskByIdUseCase
from src.domain.use_cases.tasks.get_tasks_by_project import GetTasksByProjectUseCase
from src.domain.use_cases.tasks.update_task_status import UpdateTaskStatusUseCase
from src.domain.use_cases.tasks.assign_task import AssignTaskUseCase
from src.domain.use_cases.tasks.delete_task import DeleteTaskUseCase

DbSession = Annotated[AsyncSession, Depends(get_db)]

# Users
def get_create_user(db: DbSession) -> CreateUserUseCase:
    return CreateUserUseCase(UserRepositoryImpl(db))

def get_user_by_id(db: DbSession) -> GetUserByIdUseCase:
    return GetUserByIdUseCase(UserRepositoryImpl(db))

def get_all_users(db: DbSession) -> GetAllUsersUseCase:
    return GetAllUsersUseCase(UserRepositoryImpl(db))

def get_delete_user(db: DbSession) -> DeleteUserUseCase:
    return DeleteUserUseCase(UserRepositoryImpl(db))


def get_authenticate_user(db: DbSession) -> AuthenticateUserUseCase:
    return AuthenticateUserUseCase(UserRepositoryImpl(db))

# Projects
def get_create_project(db: DbSession) -> CreateProjectUseCase:
    return CreateProjectUseCase(ProjectRepositoryImpl(db))

def get_project_by_id(db: DbSession) -> GetProjectByIdUseCase:
    return GetProjectByIdUseCase(ProjectRepositoryImpl(db))

def get_all_projects(db: DbSession) -> GetAllProjectsUseCase:
    return GetAllProjectsUseCase(ProjectRepositoryImpl(db))

def get_add_member(db: DbSession) -> AddProjectMemberUseCase:
    return AddProjectMemberUseCase(ProjectRepositoryImpl(db))

def get_project_members(db: DbSession) -> GetProjectMembersUseCase:
    return GetProjectMembersUseCase(ProjectRepositoryImpl(db))

def get_delete_project(db: DbSession) -> DeleteProjectUseCase:
    return DeleteProjectUseCase(ProjectRepositoryImpl(db))

# Tasks
def get_create_task(db: DbSession) -> CreateTaskUseCase:
    return CreateTaskUseCase(TaskRepositoryImpl(db))

def get_task_by_id(db: DbSession) -> GetTaskByIdUseCase:
    return GetTaskByIdUseCase(TaskRepositoryImpl(db))

def get_tasks_by_project(db: DbSession) -> GetTasksByProjectUseCase:
    return GetTasksByProjectUseCase(TaskRepositoryImpl(db))

def get_update_task_status(db: DbSession) -> UpdateTaskStatusUseCase:
    return UpdateTaskStatusUseCase(TaskRepositoryImpl(db))

def get_assign_task(db: DbSession) -> AssignTaskUseCase:
    return AssignTaskUseCase(TaskRepositoryImpl(db))

def get_delete_task(db: DbSession) -> DeleteTaskUseCase:
    return DeleteTaskUseCase(TaskRepositoryImpl(db))
