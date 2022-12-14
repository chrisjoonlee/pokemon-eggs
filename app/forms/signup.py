from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class SignUpForm(FlaskForm):
    username = StringField("Username", [DataRequired()])
    name = StringField("Your Name", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    confirm_password = PasswordField("Confirm Password", [DataRequired()])
    signup = SubmitField("Sign Up")
