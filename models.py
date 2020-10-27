from . import db

# Db models
class Student(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	name= db.Column(db.String, nullable=False)
	class_ = db.Column(db.Integer, nullable=True)

	def get_grades(self):
		grades = {}
		for sub in self.subjects:
			grades[sub.name] = (sub.first_half, sub.second_half, sub.final, sub.id)
		
		return grades
	
	def __repr__(self):
		return f"<Student(name='{self.name}', class={self.class_ if self.class_ else 'Unknown'})>"

class Subject(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
	
	first_half = db.Column(db.Integer)
	second_half = db.Column(db.Integer)
	final = db.Column(db.Integer)
	
	def __repr__(self):
		try:
			return f"<Subject(name='{self.name}'), student='{self.student.name}'>"
		except AttributeError:
			return f"<Subject(name='{self.name}')>"

Student.subjects = db.relationship("Subject", backref="student", lazy=True)