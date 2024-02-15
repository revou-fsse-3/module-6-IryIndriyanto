from marshmallow import Schema, fields

class AnimalSchema(Schema):
    id = fields.Int(dump_only=True)
    species = fields.Str(required=True)
    age = fields.Int(required=True)
    gender = fields.Str(required=True)