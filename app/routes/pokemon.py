from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from app.models import db, Pokemon, User

bp = Blueprint("pokemon", __name__, url_prefix="")


@bp.route("/")
@login_required
def index():
    return render_template("pokemon.html")
