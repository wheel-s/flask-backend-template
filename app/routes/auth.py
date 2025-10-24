from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.extensions import db,limiter
from app.models.user import User    
from app.schema.user_schema import UserSchema


from markupsafe import escape
auth_bp = Blueprint("auth_bp", __name__, url_prefix="/api/auth")

user_schema = UserSchema()




@auth_bp.route("/register", methods=["POST"])
@limiter.limit("5 per minute")
def register():
    data = request.get_json()
    errors = user_schema.validate(data)
    if errors:
        return {"errors", errors}, 404
    if User.query.filter_by(email =data["email"]).first():
        return {"error":" Email already exists"}, 400

    user = User(
        username= data["username"],
        email = data["email"],

        password_hash = generate_password_hash(data["password"]),
        role = data.get("role", "student")
        
    )
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user), 201



@auth_bp.route("/login", methods=["POST"])
@limiter.limit("5 per minute")
def login():
    data = request.get_json()
    user = User.query.filter_by(email =data.get("email")).first()
    if not user or not check_password_hash(user.password_hash, data.get("password")):
        return {"error":" Email  or Password not corred please provide valid details"}, 400
    token = create_access_token(identity= {"id": user.id, "role": user.role})
    return {"access-token": token}, 200


