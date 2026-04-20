from app.services.workspace_service import WorkspaceService


def test_move_user_updates_station_and_status() -> None:
    service = WorkspaceService()

    moved_user = service.move_user_to_station(user_id=1, station_id=6)

    assert moved_user.current_station_id == 6
    assert moved_user.status == "blocked"


def test_move_user_creates_activity_log_entry() -> None:
    service = WorkspaceService()
    original_count = len(service.list_activity())

    service.move_user_to_station(user_id=2, station_id=2)

    assert len(service.list_activity()) == original_count + 1
    latest_event = service.list_activity()[0]
    assert latest_event.type == "avatar_moved"
    assert latest_event.metadata["station"] == "Review Desk"
