import pytest
from utils.helpers import pet_payload


class TestPet:
    def test_criar_pet(self, client):
        payload = pet_payload()
        resp = client.post("/pet", json=payload)
        assert resp.status_code == 200
        data = resp.json()
        assert data["name"] == payload["name"]
        assert data["status"] == payload["status"]

    def test_buscar_pet_por_id(self, client, created_pet):
        resp = client.get(f"/pet/{created_pet['id']}")
        assert resp.status_code == 200
        assert resp.json()["id"] == created_pet["id"]

    def test_atualizar_pet(self, client, created_pet):
        updated = {**created_pet, "name": "updated_name", "status": "sold"}
        resp = client.put("/pet", json=updated)
        assert resp.status_code == 200
        assert resp.json()["name"] == "updated_name"
        assert resp.json()["status"] == "sold"

    def test_buscar_pets_por_status(self, client):
        for status in ["available", "pending", "sold"]:
            resp = client.get("/pet/findByStatus", params={"status": status})
            assert resp.status_code == 200
            assert isinstance(resp.json(), list)

    def test_deletar_pet(self, client):
        payload = pet_payload()
        pet = client.post("/pet", json=payload).json()
        resp = client.delete(f"/pet/{pet['id']}")
        assert resp.status_code == 200

    def test_atualizar_pet_via_formulario(self, client, created_pet):
        """Testa o endpoint de atualização via form-data (POST /pet/{id})."""
        resp = client.post(
            f"/pet/{created_pet['id']}",
            data={"name": "pet_nome_novo", "status": "pending"},
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        assert resp.status_code == 200
