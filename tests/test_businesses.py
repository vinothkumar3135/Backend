def test_requires_auth(client):
    assert client.get("/api/businesses").status_code == 401


def test_crud(client, auth_headers):
    r = client.post("/api/businesses", json={"name": "Cafe"}, headers=auth_headers)
    assert r.status_code == 201
    bid = r.json()["id"]
    assert len(client.get("/api/businesses", headers=auth_headers).json()) == 1
    assert client.get(f"/api/businesses/{bid}", headers=auth_headers).json()["name"] == "Cafe"
    assert client.delete(f"/api/businesses/{bid}", headers=auth_headers).status_code == 204
    assert client.get(f"/api/businesses/{bid}", headers=auth_headers).status_code == 404
