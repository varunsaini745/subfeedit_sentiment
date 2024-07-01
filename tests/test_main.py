from unittest.mock import patch
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


@patch("requests.get")
def test_root(mock_get):
    response = client.get("/api/")
    assert response.status_code == 200
    assert response.json() == {"message": "Server running correctly"}


@patch("requests.get")
def test_post_sentiment_data_default(mock_get):
    # Mock the response data
    mock_get.return_value.json.return_value = {
        "comments": [
            {
                "id": 1,
                "username": "user_0",
                "text": "it looks great",
                "created_at": "1719569763",
            },
            {
                "id": 2,
                "username": "user_1",
                "text": "it looks great",
                "created_at": "1719566163",
            },
        ]
    }
    response = client.post(
        "api/subfeddits/commentSentiment",
        json={
            "url": "http://0.0.0.0:8080/api/v1/comments",
            "subfeddit_id": 0,
            "skip": 0,
            "limit": 25,
        },
    )
    print("Response JSON (default):", response.json())
    assert response.status_code == 200
    assert response.json() == response.json()


@patch("requests.get")
def test_post_sorting_data(mock_get):
    mock_get.return_value.json.return_value = {
        "comments": [
            {
                "id": 1,
                "username": "user_0",
                "text": "it looks great",
                "created_at": "1719569763",
            },
            {
                "id": 2,
                "username": "user_1",
                "text": "it looks great",
                "created_at": "1719566163",
            },
        ]
    }
    url = "http://0.0.0.0:8080/api/v1/comments"
    response = client.post(
        "/api/subfeddits/commentsorting",
        json={
            "url": url,
            "sorting_parameter": "polarity",
            "subfeddit_id": 1,
            "skip": 0,
            "limit": 5,
            "start_time": 0,
            "end_time": 0,
        },
    )
    assert response.status_code == 200
    assert response.json() == response.json()
