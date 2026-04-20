"""Application service for CollabWorld workspace state.

Why this file exists:
- keeps API handlers thin and readable
- demonstrates a service boundary before introducing DB sessions
- centralizes future workflow transition rules
"""

from __future__ import annotations

from datetime import datetime, timezone

from app.domain.models import ActivityLog, Station, Task, User, Workspace


class WorkspaceService:
    """Provides read and mutation methods for MVP workspace operations."""

    def __init__(self) -> None:
        # Early-phase in-memory store used for learning and rapid iteration.
        self._workspace = Workspace(
            id=1,
            name="Demo Workspace",
            description="Starter workspace for CollabWorld MVP",
            configuration_settings={"theme": "retro-office"},
        )
        self._stations = [
            Station(1, 1, "Focus Desk", "focus", 2, 2, "in_progress"),
            Station(2, 1, "Review Desk", "review", 6, 2, "in_review"),
            Station(3, 1, "QA Desk", "qa", 10, 2, "validation"),
            Station(4, 1, "Meeting Room", "meeting", 6, 6, "sync"),
            Station(5, 1, "Delivery Desk", "delivery", 10, 6, "complete"),
            Station(6, 1, "Help Desk", "help", 2, 6, "blocked"),
        ]
        self._users = [
            User(1, "Ari", "Engineer", "🧑‍💻", "online", current_station_id=1, current_task_id=1),
            User(2, "Sam", "Project Manager", "🧑‍💼", "online", current_station_id=4, current_task_id=2),
        ]
        self._tasks = [
            Task(1, 1, "Build health endpoint", "Expose /health for uptime checks", 1, "in_progress", 45, None, 1),
            Task(2, 1, "Draft kickoff agenda", "Prepare first weekly sync agenda", 2, "planning", 20, None, 4),
        ]
        self._activity_logs: list[ActivityLog] = [
            ActivityLog(
                id=1,
                actor_id=1,
                type="avatar_moved",
                metadata={"station": "Focus Desk"},
                created_at=datetime.now(timezone.utc),
            )
        ]

    def get_workspace(self) -> Workspace:
        return self._workspace

    def list_stations(self) -> list[Station]:
        return self._stations

    def list_users(self) -> list[User]:
        return self._users

    def list_tasks(self) -> list[Task]:
        return self._tasks

    def list_activity(self) -> list[ActivityLog]:
        return self._activity_logs

    def move_user_to_station(self, user_id: int, station_id: int) -> User:
        """Moves a user and logs activity.

        Non-obvious design note:
        this mutation is where workflow transition constraints will live once
        status/state rules are expanded in later phases.
        """

        user = next((candidate for candidate in self._users if candidate.id == user_id), None)
        station = next((candidate for candidate in self._stations if candidate.id == station_id), None)

        if user is None:
            raise ValueError(f"User {user_id} not found")
        if station is None:
            raise ValueError(f"Station {station_id} not found")

        user.current_station_id = station_id
        user.status = station.workflow_behavior

        self._activity_logs.insert(
            0,
            ActivityLog(
                id=len(self._activity_logs) + 1,
                actor_id=user.id,
                type="avatar_moved",
                metadata={"station": station.name, "status": user.status},
                created_at=datetime.now(timezone.utc),
            ),
        )
        return user
