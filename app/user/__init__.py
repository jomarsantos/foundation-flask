from app.base_model import Base
from app.main import db
from passlib.apps import custom_app_context

class User(Base):

    __tablename__ = 'user'

    # Identification
    username = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192))

    # Information
    email = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    birthday = db.Column(db.Date(), nullable=False)
    city = db.Column(db.String(128), nullable=True)
    country = db.Column(db.String(128), nullable=True)

    def __repr__(self):
        return '<User %s>' % (self.username)

    def hash_password(self, password):
        self.password = custom_app_context.encrypt(password)

    def verify_password(self, password):
        return custom_app_context.verify(password, self.password)
