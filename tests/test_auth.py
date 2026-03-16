from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_login_returns_token():
    user_payload = {
        "name": "Test User",
        "email": "test@example.com",
        "password": "test1234",
        "is_active": True,
    }
    create_response = client.post("/users", json=user_payload)
    assert create_response.status_code == 201

    login_data = {
        "username": user_payload["email"],
        "password": user_payload["password"],
    }
    login_response = client.post("/auth/token", data=login_data)
    assert login_response.status_code == 200

    body = login_response.json()
    assert "access_token" in body
    assert body["token_type"] == "bearer"
