from flask import Flask
from config import Config
from flask_cors import CORS, cross_origin
# from db import db


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    # db.init_app(app)
    return app


app = create_app()


from views import index
