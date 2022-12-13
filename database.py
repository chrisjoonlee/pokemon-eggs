from app.models import User, Pokemon
from dotenv import load_dotenv
load_dotenv()

from app import app, db  # noqa

with app.app_context():
    db.drop_all()
    db.create_all()

    # Seed users
    ash = User(username="ash", name="Ash")
    ash.password = "ash"
    misty = User(username="misty", name="Misty")
    misty.password = "misty"
    brock = User(username="brock", name="Brock")
    brock.password = "brock"

    users = [ash, misty, brock]
    db.session.add_all(users)
    db.session.commit()

    pokemon = [
        Pokemon(id=1, name="Bulbasaur", img_url="", type1="Grass",
                type2="Poison", evolution_id=2, evolution_lvl=16, description="")
    ]
