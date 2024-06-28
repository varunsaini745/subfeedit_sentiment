from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/api/")
    assert response.status_code == 200
    assert response.json() == {"message": "Server running correctly"}

def test_get_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = client.get(f"/api/subfeddits?url={url}&subfeddit_id=1&skip=0&limit=5")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_post_sentiment_data():
    url = "http://0.0.0.0:8080/api/v1/comments"
    response = client.post("/api/subfeddits/commentSentiment", json={"url": url, "subfeddit_id": 1, "skip": 0, "limit": 5})
    assert response.status_code == 200
    assert "sentiment" in response.json()

def test_post_sorting_data():
    url = "http://0.0.0.0:8080/api/v1/comments"
    response = client.post("/api/subfeddits/commentsorting", json={"url": url, "sorting_parameter": "polarity", "subfeddit_id": 1, "skip": 0, "limit": 5, "start_time": 0, "end_time": 0})
    assert response.status_code == 200
    assert "sorted_comments" in response.json()
