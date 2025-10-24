from marshmallow import Schema, fields, validate
from .user_schema import UserSchema
from .course_schema import CourseSchema
from .grade_schema import GradeSchema


class StudentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=2))
    user_id = fields.Int(required=True)
    user = fields.Nested(UserSchema, dump_only=True)
    courses = fields.Nested(CourseSchema, many=True, dump_only=True)
    grades = fields = fields.Nested(GradeSchema, many =True , dump_only=True)
