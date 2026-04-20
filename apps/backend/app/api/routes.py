"""HTTP routes for initial CollabWorld backend APIs."""

from fastapi import APIRouter, HTTPException

from app.api.schemas import (
    ActivityResponse,
    MoveUserRequest,
    StationResponse,
    TaskResponse,
    UserResponse,
    WorkspaceResponse,
)
from app.services.workspace_service import WorkspaceService

router = APIRouter()
service = WorkspaceService()


@router.get("/workspace", response_model=WorkspaceResponse)
def get_workspace() -> WorkspaceResponse:
    return WorkspaceResponse.model_validate(service.get_workspace().__dict__)


@router.get("/stations", response_model=list[StationResponse])
def list_stations() -> list[StationResponse]:
    return [StationResponse.model_validate(station.__dict__) for station in service.list_stations()]


@router.get("/users", response_model=list[UserResponse])
def list_users() -> list[UserResponse]:
    return [UserResponse.model_validate(user.__dict__) for user in service.list_users()]


@router.get("/tasks", response_model=list[TaskResponse])
def list_tasks() -> list[TaskResponse]:
    return [TaskResponse.model_validate(task.__dict__) for task in service.list_tasks()]


@router.get("/activity", response_model=list[ActivityResponse])
def list_activity() -> list[ActivityResponse]:
    return [ActivityResponse.model_validate(log.__dict__) for log in service.list_activity()]


@router.post("/users/{user_id}/move", response_model=UserResponse)
def move_user(user_id: int, payload: MoveUserRequest) -> UserResponse:
    try:
        user = service.move_user_to_station(user_id=user_id, station_id=payload.station_id)
        return UserResponse.model_validate(user.__dict__)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error
