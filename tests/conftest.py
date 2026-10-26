import os

os.environ["DATABASE_URL"] = "sqlite:///./test.db"

import pytest
from fastapi.testclient import TestClient

from app.database.session import Base, engine
from app.main import app


@pytest.fixture()
def client():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c


@pytest.fixture()
def auth_headers(client):
    client.post("/api/auth/register", json={"email": "a@b.com", "password": "password123"})
    r = client.post("/api/auth/login", data={"username": "a@b.com", "password": "password123"})
    return {"Authorization": f"Bearer {r.json()['access_token']}"}
