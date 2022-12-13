from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)
    exp = db.Column(db.Integer, nullable=False)

    user_pokemon = db.relationship(
        "UserPokemon", back_populates="user", cascade="all, delete-orphan")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Pokemon(db.Model):
    __tablename__ = "pokemon"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    img_url = db.Column(db.String(255), nullable=False)
    type1 = db.Column(db.String(50), nullable=False)
    type2 = db.Column(db.String(50))
    baby = db.Column(db.Boolean, nullable=False, default=False)
    evolution_id = db.Column(db.Integer)
    evolution_lvl = db.Column(db.Integer)
    description = db.Column(db.String(1000), nullable=False)

    user_pokemon = db.relationship(
        "UserPokemon", back_populates="pokemon", cascade="all, delete-orphan")


class UserPokemon(db.Model):
    __tablename__ = "user_pokemon"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.id"), nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey(
        "pokemon.id"), nullable=False)
    nickname = db.Column(db.String(50))
    time_received = db.Column(db.DateTime(timezone=True), nullable=False)
    time_hatched = db.Column(db.DateTime(timezone=True))
    level = db.Column(db.Integer, nullable=False)

    user = db.relationship(
        "User", back_populates="user_pokemon")
    pokemon = db.relationship(
        "Pokemon", back_populates="user_pokemon")

    @staticmethod
    def train(user_id):
        # Get user's pokemon
        users_pokemon = UserPokemon \
            .query \
            .join(User) \
            .filter(and_(UserPokemon.user_id == user_id, UserPokemon.level > 0)) \
            .all()

        # Level up all pokemon by 1
        for user_pokemon in users_pokemon:
            if user_pokemon.level < 100:
                user_pokemon.level += 1

            # Check for evolution
            if user_pokemon.pokemon.evolution_lvl and user_pokemon.level >= user_pokemon.pokemon.evolution_lvl:
                user_pokemon.pokemon_id = user_pokemon.pokemon.evolution_id

        db.session.commit()
