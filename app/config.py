from dotenv import load_dotenv
import os

load_dotenv()


class Configuration:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DB_URL") or "postgresql://qxmzpaxzqmljve:d4d6cff99a51e8fd8850f3054eccc755521709d318a4430589a52ce202e136df@ec2-54-157-79-121.compute-1.amazonaws.com:5432/de7adt4c0oeav1"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
