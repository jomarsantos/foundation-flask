from app.base_model import Base
from app.main import db

class User(Base):

    __tablename__ = 'user'

    # Identification
    username = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)

    # Information
    email = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    birthday = db.Column(db.Date(), nullable=False)
    city = db.Column(db.String(128), nullable=True)
    country = db.Column(db.String(128), nullable=True)

    def __repr__(self):
        return '<User %e>' % (self.username)
