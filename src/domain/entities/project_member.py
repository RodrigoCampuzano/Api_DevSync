from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class ProjectMember:
    project_id: UUID
    user_id: UUID
    role: str  # 'ADMIN' | 'DEVELOPER'
    joined_at: datetime
