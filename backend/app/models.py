from app import db

class SellerInfo(db.Model):
    seller_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seller_name = db.Column(db.String(150), nullable=False)
    seller_profile_pic = db.Column(db.String, nullable=True)
    seller_phone_number = db.Column(db.BigInteger, nullable=False)
    seller_address = db.Column(db.String, nullable=False)
    seller_hour = db.Column(db.String, nullable=False)#Json
    seller_email = db.Column(db.String, nullable=False)
    seller_register_ts = db.Column(db.BigInteger, nullable=False)
    seller_num_followers = db.Column(db.BigInteger, nullable=False)
    seller_posted_feeds_id = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<SellerInfo {self.seller_name}>'
    
class UserInfo(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(150), unique=True, nullable=False)
    user_email = db.Column(db.String(150), unique=True, nullable=False)
    user_password = db.Column(db.String(150), nullable=False)
    user_register_ts = db.Column(db.BigInteger, nullable=False)
    user_address = db.Column(db.String, nullable=False)
    user_phone_number = db.Column(db.BigInteger, nullable=False)
    user_gender = db.Column(db.Integer, nullable=False)
    user_region = db.Column(db.String, nullable=False)
    user_profile_pic = db.Column(db.String, nullable=False)
    #List
    user_liked_feeds_ids = db.Column(db.String, nullable=False)
    user_followed_seller_ids = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<UserInfo {self.user_name}>'
    
class FeedsInfo(db.Model):
    feeds_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    feeds_seller_id = db.Column(db.Integer, nullable=False)
    feeds_imgVid_url = db.Column(db.String(150), nullable=False)
    feeds_caption = db.Column(db.String(150), nullable=False)
    feeds_ts = db.Column(db.BigInteger, nullable=False)
    feeds_num_likes = db.Column(db.BigInteger, nullable=False)

    def __repr__(self):
        return f'<FeedsInfo {self.feeds_id}>'
    
class PunchCardInfo(db.Model):
    punchCard_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    punchCard_seller_id = db.Column(db.Integer, nullable=False)
    punchCard_user_id = db.Column(db.Integer, nullable=False)
    punchCard_total_num_punch = db.Column(db.Integer, nullable=False)
    punchCard_cur_num_punch = db.Column(db.Integer, nullable=False)
    punchCard_valid = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<PunchCardInfo {self.punchCard_id}>'

class StampCardInfo(db.Model):
    stampCard_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stampCard_seller_id = db.Column(db.Integer, nullable=False)
    stampCard_user_id = db.Column(db.Integer, nullable=False)
    stampCard_total_num_stamps = db.Column(db.Integer, nullable=False)
    stampCard_cur_num_stamps = db.Column(db.Integer, nullable=False)
    stampCard_valid = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<StampCardInfo {self.stampCard_id}>'

class UserInteractionInfo(db.Model):
    userInteraction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userInteraction_user_id = db.Column(db.Integer, primary_key=True)
    userInteraction_type = db.Column(db.Integer, nullable=False)#1:Punch,2:Stamp,3:Follow,4:Like
    userInteraction_sellerId = db.Column(db.Integer, nullable=False)
    userInteraction_feedId = db.Column(db.Integer, nullable=False)
    userInteraction_punchCardId = db.Column(db.Integer, nullable=False)
    userInteraction_stampCardId = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<UserInteractionInfo {self.userInteraction_id}>'