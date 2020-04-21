from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, PasswordField
from wtforms.validators import DataRequired,InputRequired, Email, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=2, max=100)])
    password = PasswordField('Password', validators=[InputRequired()])
    

class UserForm(FlaskForm):
    fname=StringField('First Name',validators=[DataRequired(), Length(min=2, max=100)])
    lname=StringField('Last Name',validators=[DataRequired(), Length(min=2, max=100)])
    gender = SelectField(label='Gender', choices=[("M", "Male"), ("F", "Female")])
    email=StringField('Email',validators=[DataRequired()])
    location=StringField('Location',validators=[DataRequired()])
    biography=TextAreaField('Biography', validators=[Length(min=10, max=1000)])
    upload = FileField('Profile Photo', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg','gif','tiff','jfif', 'Images only!'])])
