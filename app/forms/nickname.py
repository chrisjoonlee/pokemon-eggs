from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class NicknameForm(FlaskForm):
    nickname = StringField("Nickname")
    submit = SubmitField("Enter")
