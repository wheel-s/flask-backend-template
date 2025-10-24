from marshmallow import Schema, fields, validate




class GradeSchema(Schema):
    id = fields.Int(dump_only= True, load_only=True)
    score = fields.Str( validate=validate.OneOf(["A", "B","C", "D", "E", "F"]))
    student_id = fields.Int(required=True, load_only=True)
    num = fields.Int(required=True)
    course= fields.Str(required=True)