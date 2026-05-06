import pytest
from utils.helpers import pet_payload


class TestPet:
    def test_create_pet(self, client):
        payload = pet_payload()
        resp = client.post("/pet", json=payload)
        assert resp.status_code == 200
        data = resp.json()
        assert data["name"] == payload["name"]
        assert data["status"] == payload["status"]

    def test_get_pet_by_id(self, client, created_pet):
        resp = client.get(f"/pet/{created_pet['id']}")
        assert resp.status_code == 200
        assert resp.json()["id"] == created_pet["id"]

    def test_update_pet(self, client, created_pet):
        updated = {**created_pet, "name": "updated_name", "status": "sold"}
        resp = client.put("/pet", json=updated)
        assert resp.status_code == 200
        assert resp.json()["name"] == "updated_name"
        assert resp.json()["status"] == "sold"

    def test_find_pets_by_status(self, client):
        for status in ["available", "pending", "sold"]:
            resp = client.get("/pet/findByStatus", params={"status": status})
            assert resp.status_code == 200
            assert isinstance(resp.json(), list)

    def test_delete_pet(self, client):
        payload = pet_payload()
        pet = client.post("/pet", json=payload).json()
        resp = client.delete(f"/pet/{pet['id']}")
        assert resp.status_code == 200

    def test_get_nonexistent_pet(self, client):
        resp = client.get("/pet/999999999999")
        assert resp.status_code == 404
