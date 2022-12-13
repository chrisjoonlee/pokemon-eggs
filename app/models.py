from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


user_pokemon = db.Table(
    "user_pokemon",
    db.Model.metadata,
    db.Column("user.id",
              db.ForeignKey("users.id"),
              primary_key=True,
              nullable=False),
    db.Column("pokemon_id",
              db.ForeignKey("pokemon.id"),
              primary_key=True,
              nullable=False),
    db.Column("nickname", db.String(50)),
    db.Column("time_hatched",
              db.DateTime(timezone=True),
              nullable=False)

)


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)

    pokemon = db.relationship(
        "Pokemon", secondary=user_pokemon, back_populates="users")

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
    baby = db.Column(db.Boolean, nullable=False)
    evolution_id = db.Column(db.Integer)
    evolution_lvl = db.Column(db.Integer)
    description = db.Column(db.String(1000), nullable=False)

    users = db.relationship(
        "User", secondary=user_pokemon, back_populates="pokemon")
