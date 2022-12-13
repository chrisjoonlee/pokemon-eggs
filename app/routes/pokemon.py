from datetime import datetime
from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from random import random

from app.models import db, Pokemon, User, UserPokemon

from app.settings import settings

bp = Blueprint("pokemon", __name__, url_prefix="/pokemon")


@bp.route("/")
@login_required
def index():
    print("EXP:", current_user.exp)

    users_pokemon = UserPokemon \
        .query \
        .join(User) \
        .join(Pokemon) \
        .filter(UserPokemon.user_id == current_user.id) \
        .order_by(UserPokemon.id.desc()) \
        .all()

    # users_pokemon = user_pokemon.filter(
    #     user_pokemon.user_id == current_user.id).all()

    return render_template("pokemon.html",
                           users=User.query.all(),
                           users_pokemon=users_pokemon,
                           exp=current_user.exp,
                           clicks_per_egg=settings['clicks_per_egg'])

# POST route for /pokemon/new


@bp.route("/<id>")
@login_required
def pokemon_details(id):
    return f"<h1>{id}</h1>"


@bp.route("/new", methods=["POST"])
@login_required
def new_egg():
    # Add egg to user
    new_pokemon = UserPokemon(user_id=current_user.id,
                              pokemon_id=0,
                              time_received=datetime.now(),
                              level=0)
    db.session.add(new_pokemon)
    db.session.commit()

    # Deplete the user's exp
    current_user.exp = 0
    db.session.commit()

    return redirect(url_for('.index'))


@bp.route("/fix", methods=["POST"])
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

    # Add new pokemon to user
    new_pokemon = UserPokemon(user_id=current_user.id,
                              pokemon_id=pokemon.id,
                              time_received=datetime.now(),
                              level=1)
    db.session.add(new_pokemon)
    db.session.commit()

    return redirect(url_for('.index'))


@bp.route("/train", methods=["POST"])
@ login_required
def train():
    # All pokemon level up by 1
    UserPokemon.train(current_user.id)

    # User's exp increases by 1
    current_user.exp += 1
    db.session.commit()

    return redirect(url_for('.index'))
