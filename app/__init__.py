from flask_migrate import Migrate
import yaml

from app.main import flask_app, db
import app.error_handlers

# IMPORT MODELS
import app.user

# IMPORT ROUTES
from app.user.routes import user
routes = [user]
for route in routes:
    flask_app.register_blueprint(route)

# IMPORT CONFIG
with open("./config.yaml", 'r') as stream:
    try:
        config = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# DATABASE SETUP
flask_app.config['SQLALCHEMY_DATABASE_URI'] = config['db']['uri']
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['db']['track_modifications']
db.init_app(flask_app)
migrate = Migrate(flask_app, db)
