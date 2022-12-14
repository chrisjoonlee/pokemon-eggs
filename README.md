# Pokemon Eggs

This is a simple Flask app that lets you hatch Pokemon eggs, level up Pokemon, and watch them evolve. Specifically, you can do the following:
* Sign up as a new user, log in, and log out
* Click a button to simultaneously level up all the pokemon on your team
* Receive eggs, which become available to you after a certain amount of clicks
* Hatch eggs into random 1st generation pokemon
* See the teams of all the other users registered in the app's database
* Evolve pokemon when they reach a certain level
* Give your pokemon nicknames when they hatch
* See the details of pokemon on your team
The app uses a PostgreSQL database to store data about users, pokemon, and the specific pokemon instances of each user. That means that data persists throughout sessions. If you use the app deployed on the Internet, your pokemon and the name you sign up with will be there for all other app users to see.

## What I Learned
* Flask & Python
* SQL & PostgreSQL
* SQLAlchemy & Alembic
* WTForms, CSRF Tokens, Log in systems

## How to use

### Option 1)
Go to the online app [here](https://chrisjoonlee-pokemon-eggs.herokuapp.com/)
(Deployed through Heroku)

### Option 2)

Navigate to the root folder and do the following:
* Run `pipenv install`
* Enter PSQL on your machine and create a database called `pokemon_eggs_db`
  e.g., `CREATE DATABASE pokemon_eggs_db;`
* Run `python seed_database.py`
* Run `pipenv run flask run`
* Navigate to http://localhost:5000/
