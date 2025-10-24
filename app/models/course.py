from app.extensions import db





student_courses = db.Table(
    "student_courses",
    db.Column("student_id", db.Integer, db.ForeignKey("students.id"), primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("courses.id"), primary_key=True)
)

class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable= False)
    students = db.relationship("Student",secondary = student_courses, back_populates = "courses")






