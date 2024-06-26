from db import db

class EmployeeModel_v2(db.Model):
    __tablename__ = "employee_v2"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    role = db.Column(db.String(80), nullable=False)
    schedule = db.Column(db.String(80), nullable=False)
