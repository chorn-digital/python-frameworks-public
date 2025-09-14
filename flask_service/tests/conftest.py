# flask_service/tests/conftest.py

import os, pytest
from app import create_app
from app.extensions import db as _db


@pytest.fixture(scope="session")
def app():
    os.environ["APP_ENV"] = "testing"
    app = create_app("testing")
    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()
