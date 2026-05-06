from utils.helpers import user_payload


class TestUser:
    def test_criar_usuario(self, client):
        payload = user_payload()
        resp = client.post("/user", json=payload)
        assert resp.status_code == 200

    def test_buscar_usuario_por_username(self, client, created_user):
        resp = client.get(f"/user/{created_user['username']}")
        assert resp.status_code == 200
        assert resp.json()["username"] == created_user["username"]

    def test_atualizar_usuario(self, client, created_user):
        updated = {**created_user, "firstName": "Atualizado"}
        resp = client.put(f"/user/{created_user['username']}", json=updated)
        assert resp.status_code == 200

    def test_login_usuario(self, client, created_user):
        resp = client.get(
            "/user/login",
            params={"username": created_user["username"], "password": created_user["password"]},
        )
        assert resp.status_code == 200
        assert "logged in" in resp.json()["message"].lower()

    def test_logout_usuario(self, client):
        resp = client.get("/user/logout")
        assert resp.status_code == 200

    def test_deletar_usuario(self, client):
        payload = user_payload()
        client.post("/user", json=payload)
        resp = client.delete(f"/user/{payload['username']}")
        assert resp.status_code == 200

    def test_criar_usuarios_com_array(self, client):
        users = [user_payload(), user_payload()]
        resp = client.post("/user/createWithArray", json=users)
        assert resp.status_code == 200

    def test_buscar_usuario_inexistente(self, client):
        resp = client.get("/user/usuario_que_nao_existe_xyz")
        assert resp.status_code == 404

    def test_criar_usuarios_com_lista(self, client):
        users = [user_payload() for _ in range(3)]
        resp = client.post("/user/createWithList", json=users)
        assert resp.status_code == 200
