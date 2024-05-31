from flask import request
from flask_restful import Resource
from app.models import User
from app import db

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {'username': user.username, 'email': user.email}

    def post(self):
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'], password=data['password'])
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created successfully'}, 201

def initialize_routes(api):
    api.add_resource(HelloWorld, '/')
    api.add_resource(UserResource, '/users', '/users/<int:user_id>')
