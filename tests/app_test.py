import pytest
import tempfile, os


def test_it_can_reach_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Notes" in response.data
