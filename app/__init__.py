from flask import Flask, redirect, url_for
from flask_login import LoginManager, login_required
from flask_migrate import Migrate

from .config import Configuration
from .models import db, User
from .routes import pokemon, session, users

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(pokemon.bp)
app.register_blueprint(session.bp)
app.register_blueprint(users.bp)
db.init_app(app)
migrate = Migrate(app, db)

# Configure LoginManager
login = LoginManager(app)
# Automatically redirects protected pages to the login page
login.login_view = "session.login"


# Get User objects from the database
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@login_required
@app.route("/")
def index():
    return redirect(url_for("pokemon.index"))
