import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_and_get_task():
    # Create a task
    resp = client.post("/tasks", json={"id": 0, "title": "Write tests", "completed": False})
    assert resp.status_code == 200
    data = resp.json()
    task_id = data["id"]
    assert data["title"] == "Write tests"
    # Retrieve the same task
    resp = client.get(f"/tasks/{task_id}")
    assert resp.status_code == 200
    assert resp.json()["title"] == "Write tests"

def test_list_tasks():
    resp = client.get("/tasks")
    assert resp.status_code == 200
    assert isinstance(resp.json(), dict)
