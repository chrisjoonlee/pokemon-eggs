from app.settings import settings
from app.models import Pokemon, User, UserPokemon
import json
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

from app import app, db  # noqa


with app.app_context():
    db.drop_all()
    db.create_all()

    # Seed users
    ash = User(username="ash",
               name="Ash",
               exp=settings['clicks_per_egg'])
    ash.password = "ash"
    misty = User(username="misty",
                 name="Misty",
                 exp=settings['clicks_per_egg'])
    misty.password = "misty"
    brock = User(username="brock",
                 name="Brock",
                 exp=settings['clicks_per_egg'])
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
        if 'baby' in pokemon.keys():
            new_pokemon.baby = True
        else:
            new_pokemon.baby = False
        if 'evolution_id' in pokemon.keys():
            new_pokemon.evolution_id = pokemon['evolution_id']
        if 'evolution_lvl' in pokemon.keys():
            new_pokemon.evolution_lvl = pokemon['evolution_lvl']
        pokemon_objects.append(new_pokemon)

    db.session.add_all(pokemon_objects)
    db.session.commit()

    # Add pokemon to users
    pikachu = UserPokemon(user_id=1,
                          pokemon_id=25,
                          time_received=datetime.now(),
                          time_hatched=datetime.now(),
                          level=100)

    bulbasaur = UserPokemon(user_id=1,
                            pokemon_id=1,
                            time_received=datetime.now(),
                            time_hatched=datetime.now(),
                            level=56)

    squirtle = UserPokemon(user_id=1,
                           pokemon_id=7,
                           time_received=datetime.now(),
                           time_hatched=datetime.now(),
                           level=43)

    pidgeotto = UserPokemon(user_id=1,
                            pokemon_id=16,
                            time_received=datetime.now(),
                            time_hatched=datetime.now(),
                            level=82)

    butterfree = UserPokemon(user_id=1,
                             pokemon_id=12,
                             time_received=datetime.now(),
                             time_hatched=datetime.now(),
                             level=37)

    charizard = UserPokemon(user_id=1,
                            pokemon_id=6,
                            time_received=datetime.now(),
                            time_hatched=datetime.now(),
                            level=98)

    ash_pokemon = [pikachu, bulbasaur, squirtle,
                   pidgeotto, butterfree, charizard]
    db.session.add_all(ash_pokemon)
    db.session.commit()

    staryu = UserPokemon(user_id=2,
                         pokemon_id=120,
                         time_received=datetime.now(),
                         time_hatched=datetime.now(),
                         level=42)

    starmie = UserPokemon(user_id=2,
                          pokemon_id=121,
                          time_received=datetime.now(),
                          time_hatched=datetime.now(),
                          level=66)

    psyduck = UserPokemon(user_id=2,
                          pokemon_id=54,
                          time_received=datetime.now(),
                          time_hatched=datetime.now(),
                          level=100)

    goldeen = UserPokemon(user_id=2,
                          pokemon_id=118,
                          time_received=datetime.now(),
                          time_hatched=datetime.now(),
                          level=58)

    misty_pokemon = [staryu, starmie, psyduck, goldeen]
    db.session.add_all(misty_pokemon)
    db.session.commit()

    geodude = UserPokemon(user_id=3,
                          pokemon_id=74,
                          time_received=datetime.now(),
                          time_hatched=datetime.now(),
                          level=25)

    onix = UserPokemon(user_id=3,
                       pokemon_id=95,
                       time_received=datetime.now(),
                       time_hatched=datetime.now(),
                       level=100)

    golbat = UserPokemon(user_id=3,
                         pokemon_id=42,
                         time_received=datetime.now(),
                         time_hatched=datetime.now(),
                         level=84)

    brock_pokemon = [geodude, onix, golbat]
    db.session.add_all(brock_pokemon)
    db.session.commit()
