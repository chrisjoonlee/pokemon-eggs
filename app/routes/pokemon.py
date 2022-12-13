from datetime import datetime
from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required
from random import random
from sqlalchemy import and_
from sqlalchemy.orm import joinedload

from app.models import db, Pokemon, User, UserPokemon
from app.forms.nickname import NicknameForm

from app.settings import settings

bp = Blueprint("pokemon", __name__, url_prefix="/pokemon")


@bp.route("/")
@login_required
def index():
    # Get user's pokemon
    users_pokemon = UserPokemon \
        .query \
        .options(joinedload(UserPokemon.user)) \
        .options(joinedload(UserPokemon.pokemon)) \
        .filter(UserPokemon.user_id == current_user.id) \
        .order_by(UserPokemon.id.desc()) \
        .all()

    return render_template("pokemon.html",
                           users=User.query.all(),
                           users_pokemon=users_pokemon,
                           exp=current_user.exp,
                           clicks_per_egg=settings['clicks_per_egg'])

# POST route for /pokemon/new


@bp.route("/<id>")
@login_required
def pokemon_details(id):
    user_pokemon = UserPokemon.query \
        .join(Pokemon) \
        .filter(UserPokemon.id == int(id)) \
        .first()

    return render_template("pokemon-details.html",
                           users=User.query.all(),
                           user_pokemon=user_pokemon)


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


@bp.route("/train", methods=["POST"])
@ login_required
def train():
    # All pokemon level up by 1
    new_hatch_id = UserPokemon.train(current_user.id)

    # User's exp increases by 1
    current_user.exp += 1
    db.session.commit()

    # Check if there is a new hatch
    if new_hatch_id:
        return redirect(f'/pokemon/{new_hatch_id}/new_hatch')
    else:
        return redirect(url_for('.index'))


@ bp.route("/<id>/new_hatch", methods=["GET", "POST"])
@ login_required
def new_hatch(id):
    # Fetch new pokemon
    user_pokemon = UserPokemon \
        .query \
        .join(Pokemon) \
        .filter(UserPokemon.id == int(id)) \
        .first()

    form = NicknameForm()
    if form.validate_on_submit():
        print("VALIDATED")
        nickname = form.nickname.data
        if nickname:
            user_pokemon.nickname = nickname
            db.session.commit()
        print("HEY REDIRECT")
        return redirect(url_for(".index"))

    return render_template("new-hatch.html",
                           form=form,
                           user_pokemon=user_pokemon)
