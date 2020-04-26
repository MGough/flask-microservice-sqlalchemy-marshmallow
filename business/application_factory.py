from flask import Flask
from dynaconf import FlaskDynaconf
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()
marshmallow = Marshmallow()


def create_app():
    app = Flask(__name__)
    # load in config from dynaconf
    FlaskDynaconf(app)

    marshmallow.init_app(app)
    database.init_app(app)

    with app.app_context():
        # Importing routes here avoids a circular reference
        from business.services import location_service

        database.create_all()
        app.register_blueprint(location_service.blueprint)

    return app
