import random
from utils.helpers import pet_payload


class TestStore:
    def test_buscar_inventario(self, client):
        resp = client.get("/store/inventory")
        assert resp.status_code == 200
        assert isinstance(resp.json(), dict)

    def test_criar_pedido(self, client, created_pet):
        order = {
            "id": random.randint(1, 9999),
            "petId": created_pet["id"],
            "quantity": 1,
            "status": "placed",
            "complete": True,
        }
        resp = client.post("/store/order", json=order)
        assert resp.status_code == 200
        data = resp.json()
        assert data["petId"] == created_pet["id"]
        assert data["status"] == "placed"

    def test_buscar_pedido_por_id(self, client, created_pet):
        order = {
            "id": random.randint(1, 9999),
            "petId": created_pet["id"],
            "quantity": 2,
            "status": "placed",
            "complete": False,
        }
        created = client.post("/store/order", json=order).json()
        resp = client.get(f"/store/order/{created['id']}")
        assert resp.status_code == 200
        assert resp.json()["id"] == created["id"]

    def test_deletar_pedido(self, client, created_pet):
        order = {
            "id": random.randint(1, 9999),
            "petId": created_pet["id"],
            "quantity": 1,
            "status": "placed",
            "complete": True,
        }
        created = client.post("/store/order", json=order).json()
        resp = client.delete(f"/store/order/{created['id']}")
        assert resp.status_code == 200

    def test_buscar_pedido_inexistente(self, client):
        resp = client.get("/store/order/999999999")
        assert resp.status_code == 404
