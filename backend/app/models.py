from app import db

class SellerInfo(db.Model):
    seller_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seller_name = db.Column(db.String(150), nullable=False)
    profile_pic = db.Column(db.String, nullable=True)
    phone_number = db.Column(db.BigInteger, nullable=False)
    address = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<SellerInfo {self.seller_name}>'
    
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'