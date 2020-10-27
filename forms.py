from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, ValidationError, NumberRange

# Add student form
class AddStudentForm(FlaskForm):
	name = StringField(
		"Name",
		validators=[DataRequired()]
	)
	
	class_ = IntegerField(
		"Class",
		validators=[DataRequired(),
					NumberRange(min=1, max=12)]
	)
	
	submit = SubmitField("Add Student")


# Edit student form
class EditStudentForm(FlaskForm):
	name = StringField("Edit Name")
	
	class_ = IntegerField(
		"Edit Class",
		validators=[NumberRange(min=1, max=12)]
	)
	
	submit = SubmitField("Save")


# Add subject form
class AddSubjectForm(FlaskForm):
	name = StringField(
		"Name",
		validators=[DataRequired()]
	)
	
	first_half = IntegerField(
		"First Half",
		validators=[DataRequired(),
					NumberRange(min=0, max=100)]
	)
	
	second_half = IntegerField(
		"Second Half",
		validators=[DataRequired(),
					NumberRange(min=0, max=100)]
	)
	
	final = IntegerField(
		"Final",
		validators=[DataRequired(),
					NumberRange(min=0, max=100)]
	)
	
	submit = SubmitField("Add Subject")


class EditSubjectForm(AddSubjectForm):
	submit = SubmitField("Save Changes")


