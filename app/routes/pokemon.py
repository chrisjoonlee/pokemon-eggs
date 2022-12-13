from datetime import datetime
from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from random import random

from app.models import db, Pokemon, User, UserPokemon

bp = Blueprint("pokemon", __name__, url_prefix="")


@bp.route("/")
@login_required
def index():
    users_pokemon = UserPokemon \
        .query \
        .join(User) \
        .join(Pokemon) \
        .filter(UserPokemon.user_id == current_user.id) \
        .order_by(UserPokemon.id.desc()) \
        .all()

    # users_pokemon = user_pokemon.filter(
    #     user_pokemon.user_id == current_user.id).all()

    return render_template("pokemon.html", users_pokemon=users_pokemon)

# POST route for /pokemon/new


@bp.route("/new", methods=["POST"])
@ login_required
def new_pokemon():
    # Find new baby pokemon species
    pokemon = None
    while True:
        id = int(random() * 151) + 1
        pokemon = Pokemon.query.get(id)
        if pokemon.baby:
            break

    print("POKEMON:", pokemon.name)

    # Create new pokemon
    new_pokemon = UserPokemon(user_id=current_user.id,
                              pokemon_id=pokemon.id,
                              time_received=datetime.now(),
                              level=1)
    db.session.add(new_pokemon)
    db.session.commit()

    return redirect(url_for('.index'))
    # return render_template("pokemon.html")
