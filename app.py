from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.user_resource import UsersResource, UserResource
from resources.auth_resource import SignUp, SignIn, TokenRefresh
import os
from datetime import timedelta

from utils.db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth_jwt.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']
app.config['JWT_AUTH_USERNAME_KEY'] = "username"
app.config['JWT_AUTH_PASSWORD_KEY'] = "password"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

jwt = JWTManager(app)

api = Api(app)


api.add_resource(UsersResource, '/users')
api.add_resource(UserResource, '/user/<string:username>')
api.add_resource(SignUp, '/signup')
api.add_resource(SignIn, '/signin')
api.add_resource(TokenRefresh, '/token_refresh')


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=5000, debug=True)
