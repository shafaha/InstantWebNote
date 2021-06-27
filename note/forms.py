

from flask_wtf import FlaskForm
from wtforms.validators import Length , DataRequired, Email, EqualTo, ValidationError
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField
from note.models import User, Notes




class SignupForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired(), Length(min = 4, max = 20)])
    email = StringField("Email", validators = [DataRequired(), Email(), Length(min = 4, max = 20)])
    password  = PasswordField("Password", validators = [DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo('password')])

    submit = SubmitField("SignUp")

    # we can write out custom Vaidation here
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError("Email Already present ")

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError("Username Already present ")
        

    

class LoginForm(FlaskForm):
    email = StringField("Email", validators = [DataRequired(),Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class InsertNote(FlaskForm):
    title = StringField("Title", validators = [DataRequired()])
    content = TextAreaField("Description", validators = [DataRequired()])
    submit = SubmitField("Insert")





