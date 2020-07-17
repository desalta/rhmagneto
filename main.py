from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config as config_decouple
from config import configs


def create_app(enviroment):
    app = Flask(__name__)
    db = SQLAlchemy()

    app.config.from_object(enviroment)
    db.init_app(app)
    import routes

    with app.app_context():
        db.create_all()

    return app, db


# INICIO
enviroment = configs['development']
if config_decouple('PRODUCTION', default=False):
    enviroment = configs['production']

app = Flask(__name__)
db = SQLAlchemy()

app.config.from_object(enviroment)
db.init_app(app)
import routes

with app.app_context():
    db.create_all()
