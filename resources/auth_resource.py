from flask_jwt_extended import (
    create_refresh_token, create_access_token, get_current_user, jwt_required, get_jwt_identity
)
from flask_restful import Resource
from flask import request
from models.user import User


class SignUp(Resource):
    def post(self):
        try:
            user_data = request.get_json()
            username = user_data['username']
            user = User.find_by_name(username)
            if user:
                return {"message": f"User: {username} already exist"}, 400
            user = User(**user_data)
            user.save_to_db()
            return {"message": f"User: {user} registered successfully"}
        except BaseException as e:
            return {"message": f"Error: {e}"}, 500


class SignIn(Resource):
    def post(self):
        user_data = request.get_json()
        username = user_data['username']
        user = User.find_by_name(username)
        if user and user.verify_password(user_data['password']):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        return {"message": "Invalid credentials"}, 400


class TokenRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        new_token = create_access_token(identity=identity)
        return {'access_token': new_token}, 200
