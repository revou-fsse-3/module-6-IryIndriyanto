import pytest


def test_get_animals(client):
    response = client.get("/animals_v2/")
    assert response.status_code == 200
    assert response.json is not None


def test_create_animal(client):
    data = {"species": "test_animal", "age": 6, "gender": "male"}
    response = client.post("/animals_v2/", json=data)
    assert response.status_code == 200
    assert response.json["species"] == "test_animal"


def test_get_animal(client):
    data = {"species": "test_animal", "age": 6, "gender": "male"}
    response = client.post("/animals_v2/", json=data)
    response = client.get("/animals_v2/1")
    assert response.status_code == 200
    assert response.json is not None


def test_update_animal(client):
    data = {"species": "test_animal", "age": 6, "gender": "male"}
    response = client.post("/animals_v2/", json=data)
    edited_data = {"species": "new_test_animal", "age": 6, "gender": "male"}
    response = client.put(
        "/animals_v2/1", json=edited_data
    )
    assert response.status_code == 200
    assert response.json["species"] == "new_test_animal"


def test_delete_animal(client):
    data = {"species": "test_animal", "age": 6, "gender": "male"}
    response = client.post("/animals_v2/", json=data)
    response = client.delete("/animals_v2/1")
    assert response.status_code == 200
    assert response.json["message"] == "Animal deleted"
