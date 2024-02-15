from db import db

class AnimalModel(db.Model):
    __tablename__ = "animals"

    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)