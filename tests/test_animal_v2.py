import pytest

def test_get_animals(client):
    response = client.get('/animals_v2/')
    assert response.status_code == 200
