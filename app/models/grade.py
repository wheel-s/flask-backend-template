from app.extensions import db



class Grade(db.Model):
    __tablename__ = "grades"


    id = db.Column(db.Integer, primary_key =True)
    num = db.Column(db.Integer, nullable = False)
    course= db.Column(db.String(30), nullable= False)
    score = db.Column(db.String(2) , nullable = False)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"))
    student = db.relationship("Student", back_populates = "grades")
                      