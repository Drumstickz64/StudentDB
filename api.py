from . import db
from .models import Student, Subject

# students api
def get_students():
	try:
		student_query = Student.query.all()
		students = [{"id": student.id, "name": student.name, "class": student.class_}
					for student in student_query]
		
		return students
	except Exception as e:
		print("[ERROR]", e)

def get_student(student_id):
	student_obj = Student.query.get_or_404(student_id)
	student = {
		"id": student_id,
		"name": student_obj.name,
		"class": student_obj.class_,
		"grades": student_obj.get_grades(),
	}
	return student

def add_student(name, class_):
	try:
		st = Student(name=name, class_=class_)
		db.session.add(st)
		db.session.commit()
	except Exception as e:
		print("[ERROR]", e)

def edit_student(student_id, new_name, new_class):
	student = Student.query.get_or_404(student_id)
	student.name, student.class_ = new_name, new_class
	db.session.commit()

def delete_student(student_id):
	student = Student.query.get_or_404(student_id)
	
	# Delete all of the students subjects
	for sub in student.subjects:
		db.session.delete(sub)
	
	# Delete the student
	db.session.delete(student)
	db.session.commit()


# subject api

def get_subject(subject_id):
	sub_query = Subject.query.get_or_404(subject_id)
	sub = {
		"name": sub_query.name,
		"first_half": sub_query.first_half,
		"second_half": sub_query.second_half,
		"final": sub_query.final
	}
	return sub

def add_subject(student_id, name, first_half, second_half, final):
	st = Student.query.get_or_404(student_id)
	sub = Subject(name=name, first_half=first_half,
					second_half=second_half, final=final)
					
	st.subjects.append(sub)
	db.session.commit()

def edit_subject(subject_id, name, first_half, second_half, final):
	sub = Subject.query.get_or_404(subject_id)
	
	sub.name = name
	sub.first_half = first_half
	sub.second_half = second_half
	sub.final = final
					
	db.session.commit()

def delete_subject(subject_id):
	sub = Subject.query.get_or_404(subject_id)
	db.session.delete(sub)
	db.session.commit()



