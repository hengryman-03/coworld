"""Domain entities used by the API layer in early phases.

These dataclasses intentionally mirror the product model from the project plan
so we can evolve from in-memory data to SQL-backed persistence later.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class Workspace:
    id: int
    name: str
    description: str
    configuration_settings: dict[str, Any] = field(default_factory=dict)


@dataclass
class Station:
    id: int
    workspace_id: int
    name: str
    type: str
    position_x: int
    position_y: int
    workflow_behavior: str


@dataclass
class User:
    id: int
    name: str
    role: str
    avatar: str
    status: str
    current_station_id: int | None = None
    current_task_id: int | None = None
    github_username: str | None = None


@dataclass
class Task:
    id: int
    workspace_id: int
    title: str
    description: str
    owner_id: int | None
    status: str
    progress: int
    due_date: str | None
    station_id: int | None


@dataclass
class ActivityLog:
    id: int
    actor_id: int
    type: str
    metadata: dict[str, Any]
    created_at: datetime
