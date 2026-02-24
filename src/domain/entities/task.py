from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Task:
    id: UUID
    project_id: UUID
    title: str
    description: str | None
    status: str  # 'TODO' | 'IN_PROGRESS' | 'REVIEW' | 'DONE'
    assigned_to: UUID | None
    created_by: UUID
    version: int
    updated_at: datetime
    created_at: datetime
