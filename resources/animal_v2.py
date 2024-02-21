from flask_smorest import Blueprint, abort
from models import AnimalModel_v2
from db import db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from schemas import AnimalSchema

blp = Blueprint(
    "animals_v2", "animals_v2", description="data of animals", url_prefix="/animals_v2"
)


@blp.route("/")
@blp.response(200, AnimalSchema(many=True))
def get_animals():
    return AnimalModel_v2.query.all()


@blp.route("/<int:animal_id>")
@blp.response(200, AnimalSchema)
def get_animal(animal_id):
    animal = AnimalModel_v2.query.get(animal_id)
    if animal is None:
        abort(404, "Animal not found")
    return animal


@blp.route("/", methods=["POST"])
@blp.arguments(AnimalSchema)
@blp.response(200, AnimalSchema)
def create_animal(animal_data):
    animal = AnimalModel_v2(**animal_data)

    try:
        db.session.add(animal)
        db.session.commit()
    except IntegrityError:
        abort(400, "Ensure all data is correct")
    except SQLAlchemyError:
        abort(500, "An error occurred while creating")

    return animal


@blp.route("/<int:animal_id>", methods=["PUT"])
@blp.arguments(AnimalSchema)
@blp.response(200, AnimalSchema)
def update_animal(animal_data, animal_id):
    animal = AnimalModel_v2.query.get(animal_id)
    if animal is None:
        abort(404, "Animal not found")
    AnimalModel_v2.query.filter_by(id=animal_id).update(animal_data)
    db.session.commit()
    return animal


@blp.route("/<int:animal_id>", methods=["DELETE"])
@blp.response(200)
def delete_animal(animal_id):
    animal = AnimalModel_v2.query.get(animal_id)
    if animal is None:
        abort(404, "Animal not found")
    db.session.delete(animal)
    db.session.commit()
    return {"message": "Animal deleted"}


