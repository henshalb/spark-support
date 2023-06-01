from flask import Blueprint
from flask_restful import Api
user_blueprint = Blueprint('user', __name__)
user_api = Api(user_blueprint)
from .api.auth import UserResource, UserLogin
from .api.update import UpdateUser
user_api.add_resource(UserResource, '/register')
user_api.add_resource(UserLogin, '/login')
user_api.add_resource(UpdateUser, "/user")