from app.extensions import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False, unique = True)
    email = db.Column(db.String(50), nullable = False, unique = False)
    password_hash = db.Column(db.String(198), nullable = False, )
    role = db.Column(db.String(20), default ='student')
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    students = db.relationship("Student", back_populates = "user", cascade = "all, delete-orphan")


    
    def __repr__(self):
        return f"person with {self.name} and age {self.age}"