from flask import Flask
from flask_restful import Api

from resources.user_resource import UsersResource, UserResource, SignUp
from utils.auth import identity, authenticate
import os

from utils.db import db
from flask_jwt import JWT

app = Flask(__name__)

jwt = JWT(app, authenticate, identity)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth_jwt.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']
app.config['JWT_AUTH_USERNAME_KEY'] = "username"
app.config['JWT_AUTH_PASSWORD_KEY'] = "password"

api = Api(app)


api.add_resource(UsersResource, '/users')
api.add_resource(UserResource, '/user/<string:username>')
api.add_resource(SignUp, '/signup')


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=5000, debug=True)
