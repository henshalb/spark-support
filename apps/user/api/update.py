from flask import Flask, request
from flask_restful import Api, Resource

from apps.user.model.user import User
from apps.user.schema.user import UserUpdateSchema
from apps import db


class UpdateUser(Resource):
    def put(self):
        try:
            user_id = request.args.get('id')
            user = User.query.get(user_id)
            if not user:
                return {'message': 'User not found'}, 404

            data = request.get_json()
            errors = UserUpdateSchema().validate(data)
            if errors:
                return errors, 400

            User.query.filter_by(id=user_id).update(data)
            db.session.commit()

            return {'message': 'User updated'}
        except Exception as e:
            return {'message': 'Error updating user', 'error': str(e)}, 500
