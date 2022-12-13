from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from random import random

from app.models import db, Pokemon, User

bp = Blueprint("pokemon", __name__, url_prefix="")


@bp.route("/")
@login_required
def index():
    return render_template("pokemon.html")

# POST route for /pokemon/new


@bp.route("/new", methods=["POST"])
@ login_required
def new_pokemon():
    id = int(random() * 152)
    return f"<h1>{id}</h1>"
    # return render_template("pokemon.html")
