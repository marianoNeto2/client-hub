from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def _create_user(email: str, password: str):
    payload = {
        "name": "Test User",
        "email": email,
        "password": password,
        "is_active": True,
    }
    return client.post("/users", json=payload)


def _login(email: str, password: str) -> str:
    data = {"username": email, "password": password}
    response = client.post("/auth/token", data=data)
    assert response.status_code == 200
    return response.json()["access_token"]


def test_protected_route_requires_token():
    response = client.get("/organizations")
    assert response.status_code == 401


def test_protected_route_with_token():
    email = "protected@example.com"
    password = "test1234"
    _create_user(email, password)
    token = _login(email, password)

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/organizations", headers=headers)
    assert response.status_code == 200
