"""API response models.

Pydantic is used at the boundary so clients get predictable JSON shapes while
internal domain entities remain simple dataclasses.
"""

from datetime import datetime
from pydantic import BaseModel


class WorkspaceResponse(BaseModel):
    id: int
    name: str
    description: str
    configuration_settings: dict


class StationResponse(BaseModel):
    id: int
    workspace_id: int
    name: str
    type: str
    position_x: int
    position_y: int
    workflow_behavior: str


class UserResponse(BaseModel):
    id: int
    name: str
    role: str
    avatar: str
    status: str
    current_station_id: int | None = None
    current_task_id: int | None = None
    github_username: str | None = None


class TaskResponse(BaseModel):
    id: int
    workspace_id: int
    title: str
    description: str
    owner_id: int | None
    status: str
    progress: int
    due_date: str | None
    station_id: int | None


class ActivityResponse(BaseModel):
    id: int
    actor_id: int
    type: str
    metadata: dict
    created_at: datetime


class MoveUserRequest(BaseModel):
    station_id: int
