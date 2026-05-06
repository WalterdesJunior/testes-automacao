from utils.helpers import user_payload


class TestUser:
    def test_create_user(self, client):
        payload = user_payload()
        resp = client.post("/user", json=payload)
        assert resp.status_code == 200

    def test_get_user_by_username(self, client, created_user):
        resp = client.get(f"/user/{created_user['username']}")
        assert resp.status_code == 200
        assert resp.json()["username"] == created_user["username"]

    def test_update_user(self, client, created_user):
        updated = {**created_user, "firstName": "Atualizado"}
        resp = client.put(f"/user/{created_user['username']}", json=updated)
        assert resp.status_code == 200

    def test_login(self, client, created_user):
        resp = client.get(
            "/user/login",
            params={"username": created_user["username"], "password": created_user["password"]},
        )
        assert resp.status_code == 200
        assert "logged in" in resp.json()["message"].lower()

    def test_logout(self, client):
        resp = client.get("/user/logout")
        assert resp.status_code == 200

    def test_delete_user(self, client):
        payload = user_payload()
        client.post("/user", json=payload)
        resp = client.delete(f"/user/{payload['username']}")
        assert resp.status_code == 200

    def test_create_users_with_array(self, client):
        users = [user_payload(), user_payload()]
        resp = client.post("/user/createWithArray", json=users)
        assert resp.status_code == 200

    def test_get_nonexistent_user(self, client):
        resp = client.get("/user/usuario_que_nao_existe_xyz")
        assert resp.status_code == 404
