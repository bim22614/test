from flask import Flask

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

import src.views
import src.resources.user
import src.resources.record
import src.resources.category
