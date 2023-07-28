import pytest


def test_user_can_reach_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Notes" in response.data


def test_user_can_create_a_document(client):
    response = client.post(
        "/documents/create", data={"title": "My First Note"}, follow_redirects=True
    )
    assert response.status_code == 302
    assert response.headers["Location"] == "/documents/1"
    assert b"My first note" in response.data
