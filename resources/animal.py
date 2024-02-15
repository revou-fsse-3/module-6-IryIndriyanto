from flask_smorest import Blueprint, abort
from flask.views import MethodView
from models import AnimalModel
from db import db
from sqlalchemy.exc import IntegrityError,SQLAlchemyError
from schemas import AnimalSchema

blp = Blueprint(
    "animals", "animals", description="data of animals", url_prefix="/animals"
)


@blp.route("/")
class Animals(MethodView):
    @blp.response(200, AnimalSchema (many=True))
    def get(self):
        return AnimalModel.query.all()
    @blp.arguments(AnimalSchema)
    @blp.response(200, AnimalSchema)
    def post(self, animal_data):
        animal = AnimalModel(**animal_data)

        try:
            db.session.add(animal)
            db.session.commit()
        except IntegrityError:
            abort(400, "ensure all data is correct")
        except SQLAlchemyError:
            abort(500, "an error occurred while creating")

        return animal
