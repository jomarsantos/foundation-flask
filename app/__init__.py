from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import yaml

app = Flask(__name__)

# ROUTES
from app.module_a.controllers import module_a
app.register_blueprint(module_a)

# CONFIG
with open("./app/config_app.yaml", 'r') as stream:
    try:
        config = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# DATABASE
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = config['db']['uri']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['db']['track_modifications']
db.init_app(app)
