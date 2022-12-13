import json
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

    # Import pokemon info
    file = open('pokemon-data.json')
    pokemon_data = json.load(file)
    pokemon_objects = []
    for pokemon in pokemon_data:
        new_pokemon = Pokemon(
            id=pokemon['id'],
            name=pokemon['name'],
            img_url=pokemon['img_url'],
            type1=pokemon['type1'],
            description=pokemon['description']
        )
        if 'type2' in pokemon.keys():
            new_pokemon.type2 = pokemon['type2']
        if 'evolution_id' in pokemon.keys():
            new_pokemon.evolution_id = pokemon['evolution_id']
        if 'evolution_lvl' in pokemon.keys():
            new_pokemon.evolution_lvl = pokemon['evolution_lvl']
        pokemon_objects.append(new_pokemon)

    db.session.add_all(pokemon_objects)
    db.session.commit()
