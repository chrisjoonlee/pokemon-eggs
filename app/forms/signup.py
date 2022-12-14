from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

from app.models import User


def no_duplicate_users(form, field):
    duplicate = User.query.filter_by(username=field.data).first()
    if duplicate:
        raise ValidationError("A user with this username already exists")


class SignUpForm(FlaskForm):
    username = StringField("Username", [DataRequired(), Length(
        min=4, max=25, message="Username must be between 4 and 25 characters"),
        no_duplicate_users])
    name = StringField("Your Name", [DataRequired(), Length(
        min=4, max=25, message="Username must be between 4 and 25 characters")])
    password = PasswordField(
        "Password", [DataRequired(), Length(
            min=4, max=25, message="Username must be between 4 and 25 characters")])
    confirm_password = PasswordField("Confirm Password", [
        DataRequired(), Length(
            min=4, max=25, message="Username must be between 4 and 25 characters"), EqualTo('password', message="Passwords must match")])
    signup = SubmitField("Sign Up")

    def validate_no_duplicates(self, username):
        duplicate = User.query.filter_by(username=username.data).first()
        print("Duplicate", duplicate)
        if duplicate:
            raise ValidationError("A user with this username already exists")
