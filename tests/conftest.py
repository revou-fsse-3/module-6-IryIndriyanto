import pytest
from app import create_app
from resources.animal_v2 import blp
from db import db


@pytest.fixture
def app():
    app = create_app(is_test_active=True)
    app.config.update(
        {
            "TESTING": True,
        }
    )

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
