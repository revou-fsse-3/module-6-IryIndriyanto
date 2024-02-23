import pytest


def test_get_employees(client):
    response = client.get("/employees_v2/")
    assert response.status_code == 200
    assert response.json is not None


def test_create_employee(client):
    data = {
        "name": "test_employee",
        "age": 69,
        "gender": "male",
        "role": "tiger keeper",
        "schedule": "shift 1",
    }
    response = client.post("/employees_v2/", json=data)
    assert response.status_code == 200
    assert response.json["name"] == "test_employee"


def test_get_employee(client):
    data = {
        "name": "test_employee",
        "age": 69,
        "gender": "male",
        "role": "tiger keeper",
        "schedule": "shift 1",
    }
    response = client.post("/employees_v2/", json=data)
    response = client.get("/employees_v2/1")
    assert response.status_code == 200
    assert response.json is not None


def test_update_employee(client):
    data = {
        "name": "test_employee",
        "age": 69,
        "gender": "male",
        "role": "tiger keeper",
        "schedule": "shift 1",
    }
    response = client.post("/employees_v2/", json=data)
    edited_data = {
        "name": "new_test_employee",
        "age": 69,
        "gender": "male",
        "role": "tiger keeper",
        "schedule": "shift 1",
    }
    response = client.put("/employees_v2/1", json=edited_data)
    assert response.status_code == 200
    assert response.json["name"] == "new_test_employee"


def test_delete_employee(client):
    data = {
        "name": "test_employee",
        "age": 69,
        "gender": "male",
        "role": "tiger keeper",
        "schedule": "shift 1",
    }
    response = client.post("/employees_v2/", json=data)
    response = client.delete("/employees_v2/1")
    assert response.status_code == 200
    assert response.json["message"] == "Employee deleted"
