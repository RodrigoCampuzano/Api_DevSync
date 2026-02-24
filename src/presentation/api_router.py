from fastapi import APIRouter

from src.presentation.routers.users.create_user import router as create_user_router
from src.presentation.routers.users.get_user import router as get_user_router
from src.presentation.routers.users.get_all_users import router as get_all_users_router
from src.presentation.routers.users.delete_user import router as delete_user_router

from src.presentation.routers.projects.create_project import router as create_project_router
from src.presentation.routers.projects.get_project import router as get_project_router
from src.presentation.routers.projects.get_all_projects import router as get_all_projects_router
from src.presentation.routers.projects.add_member import router as add_member_router
from src.presentation.routers.projects.get_members import router as get_members_router
from src.presentation.routers.projects.delete_project import router as delete_project_router

from src.presentation.routers.tasks.create_task import router as create_task_router
from src.presentation.routers.tasks.get_task import router as get_task_router
from src.presentation.routers.tasks.get_tasks_by_project import router as get_tasks_by_project_router
from src.presentation.routers.tasks.update_task_status import router as update_task_status_router
from src.presentation.routers.tasks.assign_task import router as assign_task_router
from src.presentation.routers.tasks.delete_task import router as delete_task_router

api_router = APIRouter()

# Users
api_router.include_router(get_all_users_router, prefix="/users", tags=["Users"])
api_router.include_router(create_user_router, prefix="/users", tags=["Users"])
api_router.include_router(get_user_router, prefix="/users", tags=["Users"])
api_router.include_router(delete_user_router, prefix="/users", tags=["Users"])

# Projects
api_router.include_router(get_all_projects_router, prefix="/projects", tags=["Projects"])
api_router.include_router(create_project_router, prefix="/projects", tags=["Projects"])
api_router.include_router(get_project_router, prefix="/projects", tags=["Projects"])
api_router.include_router(get_members_router, prefix="/projects", tags=["Projects"])
api_router.include_router(add_member_router, prefix="/projects", tags=["Projects"])
api_router.include_router(delete_project_router, prefix="/projects", tags=["Projects"])

# Tasks
api_router.include_router(get_tasks_by_project_router, prefix="/tasks", tags=["Tasks"])
api_router.include_router(create_task_router, prefix="/tasks", tags=["Tasks"])
api_router.include_router(get_task_router, prefix="/tasks", tags=["Tasks"])
api_router.include_router(update_task_status_router, prefix="/tasks", tags=["Tasks"])
api_router.include_router(assign_task_router, prefix="/tasks", tags=["Tasks"])
api_router.include_router(delete_task_router, prefix="/tasks", tags=["Tasks"])
