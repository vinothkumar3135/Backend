def test_register_and_login(client):
    r = client.post("/api/auth/register", json={"email": "x@y.com", "password": "password123"})
    assert r.status_code == 201
    r = client.post("/api/auth/login", data={"username": "x@y.com", "password": "password123"})
    assert r.status_code == 200 and "access_token" in r.json()


def test_duplicate_email(client):
    body = {"email": "x@y.com", "password": "password123"}
    client.post("/api/auth/register", json=body)
    assert client.post("/api/auth/register", json=body).status_code == 409


def test_bad_login(client):
    assert client.post("/api/auth/login", data={"username": "no@one.com", "password": "nope"}).status_code == 401
