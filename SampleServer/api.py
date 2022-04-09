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
    @api.doc(description="Get all Users")
    @api.marshal_with(user_fields, as_list=True)
    def get(self):
        return [x.__dict__ for x in User_Account.getAll()]

    @api.doc(description="Create User")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, type=str)
        args = parser.parse_args()
        User_Account.create(**args)
        return {}


@api.route("/users/<userId>")
class UserInfo(Resource):
    @api.doc(description="GET a single User")
    @api.marshal_with(user_fields)
    def get(self, userId):
        return User_Account.query.filter_by(id=userId).first().__dict__

    @api.doc(description="Update single User")
    @api.marshal_with(user_fields)
    def patch(self, userId):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str)
        args = parser.parse_args()
        User_Account.update(userId, **args)
        return User_Account.query.filter_by(id=userId).first().__dict__

    @api.doc(description="Delete single User")
    def delete(self, userId):
        User_Account.delete(userId)
        return {}

