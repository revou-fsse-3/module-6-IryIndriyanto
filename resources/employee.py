from flask_smorest import Blueprint, abort
from flask.views import MethodView
from models import EmployeeModel
from db import db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from schemas import EmployeeSchema

blp = Blueprint(
    "employees", "employees", description="data of employees", url_prefix="/employees"
)


@blp.route("/")
class Employee(MethodView):
    @blp.response(200, EmployeeSchema(many=True))
    def get(self):
        return EmployeeModel.query.all()

    @blp.arguments(EmployeeSchema)
    @blp.response(200, EmployeeSchema)
    def post(self, employee_data):
        employee = EmployeeModel(**employee_data)

        try:
            db.session.add(employee)
            db.session.commit()
        except IntegrityError:
            abort(400, "ensure all data is correct")
        except SQLAlchemyError:
            abort(500, "an error occurred while creating")

        return employee

@blp.route("/<int:employee_id>")
class Employee(MethodView):
    @blp.response(200, EmployeeSchema)
    def get(self, employee_id):
        try:
            employee = EmployeeModel.query.get(employee_id)
            return employee
        except KeyError:
            abort(404, "employee not found")

    @blp.arguments(EmployeeSchema)
    @blp.response(200, EmployeeSchema)
    def put(self, employee_data, employee_id):
        try:
            employee = EmployeeModel.query.get(employee_id)
            EmployeeModel.query.filter_by(id=employee_id).update(employee_data)
            db.session.commit()
            return employee
        except KeyError:
            abort(404, "employee not found")

    def delete(self, employee_id):
        try:
            employee = EmployeeModel.query.get(employee_id)
            db.session.delete(employee)
            db.session.commit()
            return {"massage": "employee deleted"}
        except KeyError:
            abort(404, "employee not found")


