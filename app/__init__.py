from flask import Flask, request, jsonify
from flask_migrate import Migrate
from http import HTTPStatus

import yaml

# IMPORT MODELS
from app.models import db
from app.models.user import User

# IMPORT ROUTES
from app.routes.user import user
routes = [user]

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

# HANDLE INVALID ROUTES
@app.errorhandler(HTTPStatus.NOT_FOUND.value)
def page_not_found(e):
    return jsonify({
        'msg': 'This endpoint does not exist.',
    }), HTTPStatus.NOT_FOUND

# INVALID METHODS
@app.errorhandler(HTTPStatus.METHOD_NOT_ALLOWED.value)
def method_not_allowed(e):
    return jsonify({
        'msg': 'This endpoint does not support this method.'
    }), HTTPStatus.METHOD_NOT_ALLOWED

# SERVER ERRORS
@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR.value)
def internal_server_error(e):
    return jsonify({
        'msg': 'Internal server error.',
    }), HTTPStatus.INTERNAL_SERVER_ERROR

# DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = config['db']['uri']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['db']['track_modifications']
db.init_app(app)
migrate = Migrate(app, db)
