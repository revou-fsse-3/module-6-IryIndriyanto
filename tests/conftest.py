import pytest
from flask import Flask
from resources.animal_v2 import blp
from db import db  # Import SQLAlchemy instance

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Use in-memory SQLite for tests
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(blp)
    db.init_app(app)

    with app.app_context():
        db.create_all()  # Create database tables

    return app

@pytest.fixture
def client(app):
    return app.test_client()
