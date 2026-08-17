from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_from_activity():
    activity_name = "Basketball Team"
    email = "james@mergington.edu"

    if email not in client.get("/activities").json()[activity_name]["participants"]:
        client.post(f"/activities/{activity_name}/signup?email={email}")

    response = client.delete(f"/activities/{activity_name}/participants/{email}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
    assert email not in client.get("/activities").json()[activity_name]["participants"]

    client.post(f"/activities/{activity_name}/signup?email={email}")
