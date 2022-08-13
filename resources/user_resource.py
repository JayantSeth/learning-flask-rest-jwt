from flask_restful import Resource
from models.user import User
from flask import request
from flask_jwt_extended import (
    get_current_user,
    jwt_required
)


class UsersResource(Resource):
    @jwt_required()
    def get(self):
        try:
            users = User.query.all()
            users_data = [user.json() for user in users]
            return {"users": users_data}
        except BaseException as e:
            return {"message": f"Error {e}"}, 500


class UserResource(Resource):
    @jwt_required()
    def get(self, username):
        try:
            user = User.find_by_name(username)
            if user:
                return {"user": user.json()}
            return {"message": f"User: {username} not found in database"}, 404
        except BaseException as e:
            return {"message": f"Error: {e}"}, 500

    @jwt_required()
    def put(self, username):
        try:
            user = User.find_by_name(username)
            if not user:
                return {"message": f"User: {username} does not exist in database"}, 404
            current_identity = get_current_user()
            if current_identity.username != username:
                return {"message": f"Access Denied, Only the User can updated its profile"}, 400
            user_data = request.get_json()
            if 'username' in user_data:
                user.username = user_data['username']
            if 'email' in user_data:
                user.email = user_data['email']
            if 'password' in user_data:
                user.password = user_data['password']
            user.save_to_db()
            return {"message": f"User {username} updated successfully"}
        except BaseException as e:
            return {"message": f"Error: {e}"}, 500

    @jwt_required(fresh=True)
    def delete(self, username):
        try:
            user = User.find_by_name(username)
            if not user:
                return {"message": f"User: {username} not found in database"}, 404
            user.delete_from_db()
            return {"message": f"User: {username} deleted from database"}
        except BaseException as e:
            return {"message": f"Error: {e}"}, 500
