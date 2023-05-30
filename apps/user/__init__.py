from flask import Blueprint

from .model.user import User

user_blueprint = Blueprint('user', __name__)
