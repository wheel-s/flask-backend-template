from app.extensions import db






class Student(db.Model):
    __tablename__ = "students"

    id  = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable= False, )
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", back_populates = "students")
    grades = db.relationship("Grade", back_populates = "student", cascade="all, delete-orphan") 
    courses = db.relationship("Course", secondary= "student_courses", back_populates ="students")
