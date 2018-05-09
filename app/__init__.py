from flask import Flask, request
from flask_migrate import Migrate
import yaml

# IMPORT MODELS
from app.models import db
from app.models.model_a import ModelA

# IMPORT ROUTES
from app.routes.route_a import route_a
routes = [route_a]

app = Flask(__name__)

# IMPORT CONFIG
with open("./app/config_app.yaml", 'r') as stream:
    try:
        config = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# ADD ROUTES
for route in routes:
    app.register_blueprint(route)

# DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = config['db']['uri']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['db']['track_modifications']
db.init_app(app)
migrate = Migrate(app, db)
