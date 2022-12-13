from dotenv import load_dotenv
import os

load_dotenv()


class Configuration:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
