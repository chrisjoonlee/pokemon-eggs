from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user

from app.models import User
from app.forms.login import LoginForm
from app.settings import settings

bp = Blueprint("session", __name__, url_prefix="/session")


@bp.route("/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("pokemon.index"))

    form = LoginForm()
    if form.validate_on_submit():
        # Check for user in database
        username = form.username.data
        user = User \
            .query \
            .filter(User.username == username) \
            .first()

        # If no user or invalid password
        if not user or not user.check_password(form.password.data):
            return redirect(url_for(".login"))

        login_user(user)
        return redirect(url_for("pokemon.index"))

    return render_template("login.html", form=form, img_url=settings["login_img_url"])


@bp.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return redirect(url_for(".login"))
