import pytest

from notes import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config.update({"TESTING": True})
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_it_can_reach_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Notes" in response.data
