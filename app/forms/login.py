from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from app.models import User


def user_must_exist(form, field):
    user = User.query.filter_by(username=field.data).first()
    if not user:
        raise ValidationError("User does not exist")


def check_password(form, field):
    user = User.query.filter_by(username=form.username.data).first()
    if user and not user.check_password(field.data):
        raise ValidationError("Wrong password")


class LoginForm(FlaskForm):
    username = StringField("Username", [DataRequired(), Length(
        min=4, max=25, message="Username must be between 4 and 25 characters"),
        user_must_exist])
    password = PasswordField("Password", [DataRequired(), Length(
        min=4, max=25, message="Username must be between 4 and 25 characters"),
        check_password])
    login = SubmitField("Log in")
