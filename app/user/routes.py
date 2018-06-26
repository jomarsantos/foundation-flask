import datetime
from flask import Blueprint, request, jsonify
from http import HTTPStatus
from marshmallow import ValidationError
from sqlalchemy import exc
from app.main import db, flask_app
from app.user import User
from app.user.schemas import user_schema
from app.utils.jwt_validator import login_required
from app.utils.requests import validate_request
from flask_marshmallow import pprint

user = Blueprint('user', __name__, url_prefix='/api/user')

# login
@user.route('', methods=['POST'])
def register():
    # Validate request
    user, errors = validate_request(request, user_schema)
    if errors:
        return jsonify({
            'success': False,
            'msg': 'Request parameters are invalid',
            'errors': errors
        }), HTTPStatus.OK

    # Attempt to add user
    try:
        db.session.add(user)
        db.session.commit()
    except exc.IntegrityError:
        return jsonify({
            'success': False,
            'msg': 'Account already exists for this username.',
        }), HTTPStatus.OK

    # Success, return user
    return jsonify({
        'user': user_schema.dump(user).data,
        'success': True,
        'msg': 'Successfully registered.',
    }), HTTPStatus.OK

@user.route('/test1', methods=['GET', 'POST'])
def test1():
    if request.method == 'GET':
        return "A - Test1 - GET"
    else:
        return "A - Test1 - POST"

@user.route('/test2/<param>')
@login_required
def test2(param):
    return "A - Test2 - GET - " + param

flask_app.register_blueprint(user)
