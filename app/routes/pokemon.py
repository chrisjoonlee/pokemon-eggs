from datetime import datetime
from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from random import random

from app.models import db, Pokemon, User, user_pokemon

bp = Blueprint("pokemon", __name__, url_prefix="")


@bp.route("/")
@login_required
def index():
    return render_template("pokemon.html")

# POST route for /pokemon/new


@bp.route("/new", methods=["POST"])
@ login_required
def new_pokemon():
    # Find new baby pokemon
    pokemon = None
    while True:
        id = int(random() * 152)
        pokemon = Pokemon.query.get(id)
        if pokemon.baby:
            break

    # Add to user's list of pokemon
    add_new_pokemon = user_pokemon.insert() \
        .values(user_id=current_user.id,
                pokemon_id=pokemon.id,
                time_hatched=datetime.now(),
                level=1)
    db.session.execute(add_new_pokemon)
    db.session.commit()

    print(current_user.pokemon)

    return render_template("pokemon.html")
    # return render_template("pokemon.html")
