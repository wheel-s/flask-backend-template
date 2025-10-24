from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required,get_jwt_identity
from app.models.course import Course
from app.schema.course_schema import CourseSchema
from app.extensions import db

course_bp = Blueprint("course_bp", __name__, url_prefix="/api/course")
course_schema = CourseSchema()
courses_schemas =  CourseSchema( many = True)



@course_bp.route("/course",  methods=["POST"])
@jwt_required()
def create_course():
    data = request.get_json()
    errors = course_schema.validate(data)   
    if errors:
        return {"errors", errors},404
    course  = Course(title = data["title"])
    db.session.add(course)
    db.session.commit()
  
    return course_schema.dump(course), 201


@course_bp.route("/course", methods = ["GET"])
@jwt_required()
def get_course():
    courses = Course.query.all()
    return courses_schemas.dump(courses)