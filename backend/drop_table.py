from app import create_app, db
from app.models import SellerInfo

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()
