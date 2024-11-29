from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_post():
    response = client.post(
        "/posts/",
        json={"title": "Test Post 228", "content": "This is a test post content."},
    )
    assert response.status_code == 200
    assert response.json()["title"]["title"] == "Test Post 228"
    assert response.json()["title"]["content"] == "This is a test post content."

def test_get_posts():
    response = client.get("/posts/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
