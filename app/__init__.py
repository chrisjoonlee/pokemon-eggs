from flask import Flask, redirect, render_template
from flask_migrate import Migrate

from app.config import Configuration
from app.models import db

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    return "<h1>Hello world</h1>"
