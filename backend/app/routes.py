from flask import request
from flask_restful import Resource
from app.models import SellerInfo, User
from app import db

class SellerInfoResource(Resource):
    def get(self, seller_id=None):
        if seller_id:
            seller = SellerInfo.query.get_or_404(seller_id)
            return {
                'seller_id': seller.seller_id,
                'seller_name': seller.seller_name,
                'profile_pic': seller.profile_pic,
                'phone_number': seller.phone_number,
                'address': seller.address
            }
        else:
            sellers = SellerInfo.query.all()
            return [{
                'seller_id': seller.seller_id,
                'seller_name': seller.seller_name,
                'profile_pic': seller.profile_pic,
                'phone_number': seller.phone_number,
                'address': seller.address
            } for seller in sellers]

    def post(self):
        data = request.get_json()
        new_seller = SellerInfo(
            seller_name=data['seller_name'],
            profile_pic=data.get('profile_pic'),
            phone_number=data['phone_number'],
            address=data['address']
        )
        db.session.add(new_seller)
        db.session.commit()
        return {'message': 'Seller created successfully'}, 201

    def put(self, seller_id):
        seller = SellerInfo.query.get_or_404(seller_id)
        data = request.get_json()
        seller.seller_name = data['seller_name']
        seller.profile_pic = data.get('profile_pic')
        seller.phone_number = data['phone_number']
        seller.address = data['address']
        db.session.commit()
        return {'message': 'Seller updated successfully'}, 200

    def delete(self, seller_id):
        seller = SellerInfo.query.get_or_404(seller_id)
        db.session.delete(seller)
        db.session.commit()
        return {'message': 'Seller deleted successfully'}, 200

class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            user = User.query.get_or_404(user_id)
            return {
                'user_id': user.user_id,
                'username': user.username,
                'email': user.email
            }
        else:
            users = User.query.all()
            return [{
                'user_id': user.user_id,
                'username': user.username,
                'email': user.email
            } for user in users]

    def post(self):
        data = request.get_json()
        if User.query.filter_by(email=data['email']).first():
            return {'message': 'A user with this email already exists'}, 400

        new_user = User(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created successfully'}, 201

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        user.username = data['username']
        user.email = data['email']
        user.password = data['password']
        db.session.commit()
        return {'message': 'User updated successfully'}, 200

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted successfully'}, 200

def initialize_routes(api):
    api.add_resource(SellerInfoResource, '/sellers', '/sellers/<int:seller_id>')
    api.add_resource(UserResource, '/users', '/users/<int:user_id>')
