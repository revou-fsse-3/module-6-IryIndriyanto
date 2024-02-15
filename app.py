from flask import Flask
from dotenv import load_dotenv
from flask_smorest import Api
from db import db
from resources.animal import blp as animal_blueprint
import os


def create_app():
    app = Flask(__name__)
    load_dotenv()

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "sqlite:///data.db"
    )

    db.init_app(app)
    with app.app_context():
        db.create_all()

    api = Api(app)
    api.register_blueprint(animal_blueprint)

    return app
