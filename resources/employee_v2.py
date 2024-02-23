from flask_smorest import Blueprint, abort
from models import EmployeeModel_v2
from db import db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from schemas import EmployeeSchema

blp = Blueprint(
    "employees_v2", "employees_v2", description="data of employees", url_prefix="/employees_v2"
)


@blp.route("/")
@blp.response(200, EmployeeSchema(many=True))
def get_employees():
    return EmployeeModel_v2.query.all()


@blp.route("/<int:employee_id>")
@blp.response(200, EmployeeSchema)
def get_employee(employee_id):
    employee = db.session.get(EmployeeModel_v2, employee_id)
    if employee is None:
        abort(404, "Animal not found")
    return employee


@blp.route("/", methods=["POST"])
@blp.arguments(EmployeeSchema)
@blp.response(200, EmployeeSchema)
def create_employee(employee_data):
    employee = EmployeeModel_v2(**employee_data)

    try:
        db.session.add(employee)
        db.session.commit()
    except IntegrityError:
        abort(400, "Ensure all data is correct")
    except SQLAlchemyError:
        abort(500, "An error occurred while creating")

    return employee


@blp.route("/<int:employee_id>", methods=["PUT"])
@blp.arguments(EmployeeSchema)
@blp.response(200, EmployeeSchema)
def update_employee(employee_data, employee_id):
    employee = db.session.get(EmployeeModel_v2, employee_id)
    if employee is None:
        abort(404, "Animal not found")
    EmployeeModel_v2.query.filter_by(id=employee_id).update(employee_data)
    db.session.commit()
    return employee


@blp.route("/<int:employee_id>", methods=["DELETE"])
@blp.response(200)
def delete_employee(employee_id):
    employee = db.session.get(EmployeeModel_v2, employee_id)
    if employee is None:
        abort(404, "Animal not found")
    db.session.delete(employee)
    db.session.commit()
    return {"message": "Animal deleted"}
