from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required,get_jwt_identity
from app.models.grade import Grade
from app.schema.grade_schema import GradeSchema
from app.extensions import db
from app.utils.grade import get_grade

grade_bp = Blueprint("grade_bp", __name__, url_prefix="/api/grade")


grade_schema = GradeSchema()
grades_schema =  GradeSchema( many = True)

@grade_bp.route('/', methods = ["POST"])
@jwt_required()
def create_grade():
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return {"error": "admins only route"}, 403
    data = request.get_json()
    errors = grade_schema.validate(data)   
    if errors:
        return {"errors", "please provide valid fields"}, 400
    num = data["num"]
    num_int = int(num)
    grade = get_grade(num_int)
    grade = Grade(
        score = grade,
        student_id = data["student_id"],
        num = data["num"],
        course = data["course"]
    )
    db.session.add(grade)
    db.session.commit()

    return grade_schema.dump(grade)

@grade_bp.route('/')
@jwt_required()
def get_grades():
    grades = Grade.query.all()
    return {grades_schema.dump(grades)}, 200
