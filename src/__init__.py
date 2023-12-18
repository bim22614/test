from flask import Flask

app = Flask(__name__)
import src.views
import src.resources.user
import src.resources.record
import src.resources.category
