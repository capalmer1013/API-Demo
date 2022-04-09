from flask import Flask, jsonify, request
from flask_restx import Resource, Api

from .models import *

app = Flask(__name__)
api = Api(app, title="Sample REST api")


@api.route("/users/")
class Users(Resource):
    @api.doc(
        description="Endpoints for Users"
    )
    def get(self):
        return {}

    def post(self, userId):
        models.User_Account.update_username(get_username(), userId)
        return {}


@api.route("/users/<userId>")
class UserInfo(Resource):
    @api.doc(
        description="Endpoints for a single User"
    )
    def post(self, userId):
        models.User_Account.update_username(get_username(), userId)
        return {}

