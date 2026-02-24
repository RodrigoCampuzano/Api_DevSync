from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from src.application.dependencies import get_assign_task
from src.application.schemas.task_schema import AssignTaskRequest, TaskResponse
from src.domain.use_cases.tasks.assign_task import AssignTaskUseCase
from src.presentation.websockets.manager import connection_manager

router = APIRouter()


@router.patch("/{task_id}/assign", response_model=TaskResponse)
async def assign_task(
    task_id: UUID,
    body: AssignTaskRequest,
    use_case: Annotated[AssignTaskUseCase, Depends(get_assign_task)],
):
    """Assign (or unassign) a task to a user. Broadcasts the change via WebSocket."""
    task = await use_case.execute(task_id=task_id, user_id=body.user_id)
    await connection_manager.broadcast_to_room(
        room_id=str(task.project_id),
        message={
            "event": "task_assigned",
            "task_id": str(task.id),
            "assigned_to": str(task.assigned_to) if task.assigned_to else None,
        },
    )
    return task
