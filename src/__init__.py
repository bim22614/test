from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from src.models import UserModel, RecordModel, CategoryModel


import src.views
import src.resources.user
import src.resources.record
import src.resources.category
