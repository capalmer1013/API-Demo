# stdlib imports
import os

# flask imports
from flask_migrate import Migrate
from flask import Flask

# project imports
from .models import db
from .api import app

# app setup
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
migrate = Migrate(app, db)
db.init_app(app)