from . import app, db
from .forms import (AddStudentForm, EditStudentForm,
					AddSubjectForm, EditSubjectForm)
from .api import (add_student, get_students, get_student,
					edit_student, delete_student, get_subject,
					add_subject, edit_subject, delete_subject)
from flask import render_template, url_for, redirect, request

@app.route("/", methods=["GET", "POST"])
def home():
	form = AddStudentForm()
	if form.validate_on_submit():
		name = (form.name.data).title()
		class_ = form.class_.data
		add_student(name, class_)
		return redirect(url_for("home"))
	
	students = sorted(get_students(), key=lambda st: st["name"])
	return render_template("home.html", students=students, form=form)


@app.route("/student/<int:student_id>", methods=["GET", "POST"])
def student(student_id):
	student = get_student(student_id)
	form = EditStudentForm()
	
	if request.method == "GET":
		form.name.data = student["name"]
		form.class_.data = student["class"]

	if form.validate_on_submit():
		new_name = form.name.data.title()
		new_class = form.class_.data
		edit_student(student_id, new_name, new_class)
		return redirect(url_for("student", student_id=student_id))
	
	return render_template("student.html",
							student=student, form=form)

@app.route("/student/<int:student_id>/delete", methods=["GET", "POST"])
def delete_student_page(student_id):
	delete_student(student_id)
	return redirect(url_for("home"))

@app.route("/student/<int:student_id>/subjects/add", methods=["GET", "POST"])
def add_subject_page(student_id):
	form = AddSubjectForm()
	if form.validate_on_submit():
		name = form.name.data
		first_half = form.first_half.data
		second_half = form.second_half.data
		final = form.final.data
		
		add_subject(student_id, name, first_half, second_half, final)
		return redirect(url_for("student", student_id=student_id))
	
	return render_template("subject.html", form=form)

@app.route("/student/<int:student_id>/subjects/<int:subject_id>/edit", methods=["GET", "POST"])
def edit_subject_page(student_id, subject_id):
	form = EditSubjectForm()
	sub = get_subject(subject_id)
	
	if request.method == "GET":
		form.name.data = sub["name"]
		form.first_half.data = sub["first_half"]
		form.second_half.data = sub["second_half"]
		form.final.data = sub["final"]
	
	if form.validate_on_submit():
		name = form.name.data
		first_half = form.first_half.data
		second_half = form.second_half.data
		final = form.final.data
		
		edit_subject(subject_id, name, first_half, second_half, final)
		return redirect(url_for("student", student_id=student_id))
	
	return render_template("subject.html", form=form)


@app.route("/student/<int:student_id>/subjects/<int:subject_id>/delete", methods=["GET", "POST"])
def delete_subject_page(student_id, subject_id):
	delete_subject(subject_id)
	return redirect(url_for("student", student_id=student_id))
	


