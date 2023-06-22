from fastapi.testclient import TestClient
import main
import pytest


client = TestClient(main.app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"mensagem":"Hello World!!!"}



