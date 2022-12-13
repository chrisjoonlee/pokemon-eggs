from flask import Flask, redirect, render_template
from flask_login import LoginManager
from flask_migrate import Migrate

from .config import Configuration
from .models import db, User
from .routes import session

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(session.bp)
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


@app.route("/")
def index():
    return "<h1>Hello world</h1>"
