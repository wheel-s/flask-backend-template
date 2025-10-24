from marshmallow import Schema, fields, validate




class CourseSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=2))