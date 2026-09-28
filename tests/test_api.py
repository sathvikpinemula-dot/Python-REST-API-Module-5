from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
HEADERS = {"X-API-Key": "codomax-demo-key"}

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_authentication():
    response = client.get("/students")
    assert response.status_code == 401

def test_create_and_read_student():
    email = "test_student_001@example.com"
    payload = {"name": "Test Student", "email": email, "course": "Python"}
    response = client.post("/students", json=payload, headers=HEADERS)
    assert response.status_code in (201, 409)

    students = client.get("/students", headers=HEADERS)
    assert students.status_code == 200

    if response.status_code == 201:
        student_id = response.json()["id"]
        detail = client.get(f"/students/{student_id}", headers=HEADERS)
        assert detail.status_code == 200

        delete = client.delete(f"/students/{student_id}", headers=HEADERS)
        assert delete.status_code == 200
