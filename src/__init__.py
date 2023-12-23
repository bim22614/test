from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.db import db
from .resources.user import blueprint_user
from .resources.record import blueprint_record
from .resources.category import category_blueprint


# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config.from_pyfile('config.py', silent=True)
#
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py', silent=True)
    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()

    app.register_blueprint(blueprint_user)
    app.register_blueprint(category_blueprint)
    app.register_blueprint(blueprint_record)

    return app

# from src.models import UserModel, RecordModel, CategoryModel


# import src.views
# import src.resources.user
# import src.resources.record
# import src.resources.category
