from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required,get_jwt_identity
from app.models.student import Student
from app.schema.student_schema import StudentSchema
from app.extensions import db
import app



student_bp = Blueprint("student_bp", __name__, url_prefix="/api/v1")
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)





@student_bp.route("/student")
@jwt_required()
def get_students():
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return {"error": "admins only route"}, 403
    students = Student.query.all()
    student_data = student_schema.dump(students)
    return  {"student":student_data}, 200


@student_bp.route("/student", methods=['POST'])
@jwt_required()
def create_students():
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return {"error": "admins only route"}, 403
    data = request.get_json()
    errors = student_schema.validate(data)
    if errors:
        return {"errors", errors}, 404
    id = current_user["id"]
    student = Student(
        name = data["name"],
        user_id = id
    )

    db.session.add(student)
    db.session.commit()

    return student_schema.dump(student), 201



@student_bp.route("/student/<int:id>", methods=['GET'])
@jwt_required()
def get_student(id):
   
    student = Student.query.get_or_404(id)
    if not student:
        return  {"student":"student not found"}, 404
    student_data = student_schema.dump(student)
    return  {"student":student_data}, 200








@student_bp.route("/student/<int:id>", methods= ['PATCH'])
@jwt_required()
def update_students(id):

    student = Student.query.get_or_404(id)
    data = request.get_json()
    errors = student_schema.validate(data, partial=True)
    if errors:
        return{"errors": errors} , 400
    if "name" in data:
        student.name = data["name"]
    db.session.commit()
    student_data = student_schema.dump(student)
    return  {"student":f"{student_data}"}


@student_bp.route("/student/<int:id>", methods = ['DELETE'])
@jwt_required()
def delete_students(id):
   
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()

    return {"message":" student deleted sucessfully"}







    






