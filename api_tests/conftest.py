import pytest
from utils.client import PetstoreClient
from utils.helpers import pet_payload, user_payload


@pytest.fixture(scope="session")
def client():
    return PetstoreClient()


@pytest.fixture
def created_pet(client):
    """Cria um pet e garante limpeza após o teste."""
    payload = pet_payload()
    resp = client.post("/pet", json=payload)
    assert resp.status_code == 200
    pet = resp.json()
    yield pet
    client.delete(f"/pet/{pet['id']}")


@pytest.fixture
def created_user(client):
    """Cria um usuário e garante limpeza após o teste."""
    payload = user_payload()
    resp = client.post("/user", json=payload)
    assert resp.status_code == 200
    yield payload
    client.delete(f"/user/{payload['username']}")
