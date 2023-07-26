import sys
import os, tempfile
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from notes import create_app
from notes.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), "test_seed.sql"), "rb") as f:
    test_seed_sql = f.read().decode()


@pytest.fixture
def app():
    db_f, db_path = tempfile.mkstemp()

    app = create_app()
    app.config.update({"TESTING": True, "DATABASE": db_path})
    with app.app_context():
        init_db()
        get_db().executescript(test_seed_sql)
        get_db().commit()

    yield app
    os.close(db_f)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()
