from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user
from sqlalchemy.orm import joinedload

from app.models import db, Pokemon, User, UserPokemon
from app.forms.signup import SignUpForm
from app.settings import settings

bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("/<id>")
@login_required
def other_user(id):
    print("id", id)
    print("current id", current_user.id)
    # If the user clicks their own name
    if int(id) == current_user.id:
        return redirect(url_for("pokemon.index"))

    # Get other user's pokemon
    users_pokemon = UserPokemon \
        .query \
        .options(joinedload(UserPokemon.user)) \
        .options(joinedload(UserPokemon.pokemon)) \
        .filter(UserPokemon.user_id == id) \
        .order_by(UserPokemon.id.desc()) \
        .all()

    return render_template("other-pokemon.html",
                           current_user=current_user,
                           other_user=User.query.get(id),
                           users=current_user.get_other_users(),
                           users_pokemon=users_pokemon
                           )


# Route for signing up a new user
@bp.route("/new", methods=["POST", "GET"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("pokemon.index"))

    form = SignUpForm()
    if form.validate_on_submit():
        # Create new user
        user = User(
            username=form.username.data,
            name=form.name.data,
            exp=settings['clicks_per_egg']
        )
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()

        # Login user
        login_user(user)
        return redirect(url_for("pokemon.index"))

    return render_template("signup.html",
                           form=form)
