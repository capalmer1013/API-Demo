from flask import Flask, jsonify, request, make_response
from flask_restx import Resource, Api, reqparse, fields

from .models import User_Account

app = Flask(__name__)
api = Api(app, title="Sample REST api")

user_fields = api.model(
    "User", {"id": fields.Integer, "username": fields.String}
)

@api.route("/users/")
class Users(Resource):
    @api.doc(
        description="Endpoints for Users"
    )
    @api.marshal_with(user_fields, as_list=True)
    def get(self):
        return [x.__dict__ for x in User_Account.getAll()]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, type=str)
        args = parser.parse_args()
        return {}


@api.route("/users/<userId>")
class UserInfo(Resource):
    @api.doc(
        description="Endpoints for a single User"
    )
    def get(self, userId):
        return {}

    def patch(self, userId):
        return {}

    def delete(self, userId):
        models.User_Account.delete(userId)
        return {}

