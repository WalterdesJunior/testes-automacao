import random
from utils.helpers import pet_payload


class TestStore:
    def test_get_inventory(self, client):
        resp = client.get("/store/inventory")
        assert resp.status_code == 200
        assert isinstance(resp.json(), dict)

    def test_create_order(self, client, created_pet):
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

    def test_get_order_by_id(self, client, created_pet):
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

    def test_delete_order(self, client, created_pet):
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

    def test_get_nonexistent_order(self, client):
        resp = client.get("/store/order/999999999")
        assert resp.status_code == 404
