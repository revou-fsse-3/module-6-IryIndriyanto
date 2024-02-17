from flask_smorest import Blueprint, abort
from flask.views import MethodView
from models import AnimalModel
from db import db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from schemas import AnimalSchema

blp = Blueprint(
    "animals", "animals", description="data of animals", url_prefix="/animals"
)


@blp.route("/")
class Animal(MethodView):
    @blp.response(200, AnimalSchema(many=True))
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

@blp.route("/<int:animal_id>")
class Animal(MethodView):
    @blp.response(200, AnimalSchema)
    def get(self, animal_id):
        try:
            animal = AnimalModel.query.get(animal_id)
            return animal
        except KeyError:
            abort(404, "animal not found")

    @blp.arguments(AnimalSchema)
    @blp.response(200, AnimalSchema)
    def put(self, animal_data, animal_id):
        try:
            animal = AnimalModel.query.get(animal_id)
            AnimalModel.query.filter_by(id=animal_id).update(animal_data)
            db.session.commit()
            return animal
        except KeyError:
            abort(404, "animal not found")

    def delete(self, animal_id):
        try:
            animal = AnimalModel.query.get(animal_id)
            db.session.delete(animal)
            db.session.commit()
            return {"massage": "animal deleted"}
        except KeyError:
            abort(404, "animal not found")


