import os
from flask import Flask
from dotenv import load_dotenv
from flask_smorest import Api

from resources.animal import blp as animal_blueprint
from db import db


def create_app():
    app = Flask(__name__)
    load_dotenv()

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Zoo Management REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )

    # DATABASE_URL = os.getenv("DATABASE_URL").replace("")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "sqlite:///data.db"
    )

    db.init_app(app)
    with app.app_context():
        db.create_all()

    api = Api(app)

    api.register_blueprint(animal_blueprint)

    return app
