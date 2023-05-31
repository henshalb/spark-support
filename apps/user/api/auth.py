
from flask import request, session
from flask_restful import Resource
from apps.user.service.auth import create_user, get_user
from apps.user.schema.user import UserLoginSchema, UserOutSchema, UserInSchema


class UserResource(Resource):

    def post(self):
        """
        Create user
        """
        try:
            data = request.get_json()
            errors = UserInSchema().validate(data)
            if errors:
                return errors, 400
            user = create_user(**data)
            return UserOutSchema().dump(user)
        except Exception as e:
            print(e)
            # TODO: Specific handlers
            return {"error": "Similar record exists"}, 400


class UserLogin(Resource):

    def post(self):
        """
        Login user
        """
        try:
            data = request.get_json()
            errors = UserLoginSchema().validate(data)
            if errors:
                return errors, 400
            user = get_user(data.get("email"))
            if user.check_password(data.get("password")):
                session['logged-in'] = True
                return {"message": "User logged in successfully"}, 200
            return {"message": "Password does not match"}, 400
        except Exception:
            # TODO: Specific handlers
            return {"error": "No such user"}, 404
