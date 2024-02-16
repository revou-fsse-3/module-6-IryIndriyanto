from marshmallow import Schema, fields

class AnimalSchema(Schema):
    id = fields.Int(dump_only=True)
    species = fields.Str(required=True)
    age = fields.Int(required=True)
    gender = fields.Str(required=True)

class EmployeeSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    age = fields.Int(required=True)
    gender = fields.Str(required=True)
    role = fields.Str(required=True)
    schedule = fields.Str(required=True)
