from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

flask_app = Flask(__name__)
db = SQLAlchemy()
ma = Marshmallow(flask_app)
