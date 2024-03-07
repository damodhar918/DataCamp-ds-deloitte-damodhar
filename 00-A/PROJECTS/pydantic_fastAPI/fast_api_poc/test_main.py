# test_main.py

from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app

client = TestClient(app)


def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == []  # Assuming your endpoint returns an empty list initially
