from app.models import db
from app.models.base import Base

class User(Base):

    __tablename__ = 'user'

    # Identification Data
    username = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)

    # Information
    email = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    birthday = db.Column(db.Date(), nullable=False)
    city = db.Column(db.String(128), nullable=True)
    country = db.Column(db.String(128), nullable=True)

    # New instance instantiation procedure
    def __init__(self, email, password, username, first_name, last_name,
        birthday, city, country
    ):
        self.email = email
        self.password = password
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.city = city
        self.country = country

    def __repr__(self):
        return '<User %e>' % (self.username)
