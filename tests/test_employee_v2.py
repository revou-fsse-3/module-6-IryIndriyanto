import pytest


@pytest.fixture
def employee_data():
    return {
        "name": "test_employee",
        "age": 69,
        "gender": "male",
        "role": "tiger keeper",
        "schedule": "shift 1",
    }


def test_get_employees(client):
    response = client.get("/employees_v2/")

    assert response.status_code == 200
    assert response.json is not None


def test_create_employee(client, employee_data):
    response = client.post("/employees_v2/", json=employee_data)

    assert response.status_code == 200
    assert response.json["name"] == "test_employee"


def test_get_employee(client, employee_data):
    response = client.post("/employees_v2/", json=employee_data)
    response = client.get("/employees_v2/1")

    assert response.status_code == 200
    assert response.json is not None


def test_update_employee(client, employee_data):
    response = client.post("/employees_v2/", json=employee_data)
    edited_data = {
        **employee_data,
        "name": "new_test_employee",
    }
    response = client.put("/employees_v2/1", json=edited_data)

    assert response.status_code == 200
    assert response.json["name"] == "new_test_employee"


def test_delete_employee(client, employee_data):
    response = client.post("/employees_v2/", json=employee_data)
    response = client.delete("/employees_v2/1")

    assert response.status_code == 200
    assert response.json["message"] == "Employee deleted"


def test_get_nonexistent_employee(client):
    response = client.get("/employees_v2/999")

    assert response.status_code == 404
    assert response.json["status"] == "Not Found"


def test_create_invalid_employee(client):
    invalid_data = {
        "name": "test_employee",
        "age": 69,
    }
    response = client.post("/employees_v2/", json=invalid_data)

    assert response.status_code == 422
    assert response.json["status"] == "Unprocessable Entity"
    assert (
        response.json["errors"]["json"]["role"][0] == "Missing data for required field."
    )
    assert (
        response.json["errors"]["json"]["gender"][0]
        == "Missing data for required field."
    )
    assert (
        response.json["errors"]["json"]["schedule"][0]
        == "Missing data for required field."
    )
