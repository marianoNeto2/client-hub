from uuid import uuid4

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def _create_user_and_token():
    email = f"cust_{uuid4().hex}@example.com"
    password = "test1234"
    payload = {
        "name": "Test User",
        "email": email,
        "password": password,
        "is_active": True,
    }
    create_response = client.post("/users", json=payload)
    assert create_response.status_code == 201

    login_data = {"username": email, "password": password}
    login_response = client.post("/auth/token", data=login_data)
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    return token


def _create_organization(headers):
    payload = {"name": f"Org {uuid4().hex}", "description": "Test org"}
    response = client.post("/organizations", json=payload, headers=headers)
    assert response.status_code == 201
    return response.json()


def test_customer_crud():
    token = _create_user_and_token()
    headers = {"Authorization": f"Bearer {token}"}

    organization = _create_organization(headers)

    create_payload = {
        "name": "Customer One",
        "email": "customer1@example.com",
        "phone": "11999990000",
        "organization_id": organization["id"],
    }
    create_response = client.post("/customers", json=create_payload, headers=headers)
    assert create_response.status_code == 201
    customer = create_response.json()

    get_response = client.get(f"/customers/{customer['id']}", headers=headers)
    assert get_response.status_code == 200

    update_payload = {"name": "Customer Updated"}
    update_response = client.patch(
        f"/customers/{customer['id']}",
        json=update_payload,
        headers=headers,
    )
    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Customer Updated"

    delete_response = client.delete(
        f"/customers/{customer['id']}",
        headers=headers,
    )
    assert delete_response.status_code == 204
