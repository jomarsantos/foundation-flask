import datetime
import jwt
from flask import Blueprint, request, jsonify
from http import HTTPStatus
from marshmallow import ValidationError
from sqlalchemy import exc
from app.main import db, flask_app
from app.user import User
from app.user.schemas import user_schema, user_register_request_schema, user_login_request_schema
from app.utils.jwt_validator import login_required
from app.utils.requests import validate_request
from flask_marshmallow import pprint

user = Blueprint('user', __name__, url_prefix='/api/user')

@user.route('', methods=['GET'])
@login_required
def get_self(jwt_payload):
    user = db.session.query(User).filter(User.id == jwt_payload['id']).first()

    if user is None:
        return jsonify({
            'success': False,
            'msg': 'No user exists with id %s.' % jwt_payload['id'],
        }), HTTPStatus.BAD_REQUEST

    return jsonify({
        'success': True,
        'user': user_schema.dump(user).data,
        'msg': 'Successfully found user with id %s.' % jwt_payload['id'],
    }), HTTPStatus.OK

@user.route('', methods=['POST'])
def register():
    # Validate request
    user, errors = validate_request(request, user_register_request_schema)
    if errors:
        return jsonify({
            'success': False,
            'msg': 'Request parameters are invalid',
            'error': errors
        }), HTTPStatus.BAD_REQUEST

    # Attempt to add user
    user.hash_password(request.get_json()['password'])
    try:
        db.session.add(user)
        db.session.commit()
    except exc.IntegrityError:
        return jsonify({
            'success': False,
            'msg': 'Unable to create account.',
        }), HTTPStatus.BAD_REQUEST

    # Success, return user
    user_data = user_schema.dump(user).data
    user_data.pop('password', None)
    return jsonify({
        'success': True,
        'user': user_data,
        'msg': 'Successfully registered.',
    }), HTTPStatus.OK

@user.route('/<user_id>', methods=['GET'])
@login_required
def get_user(jwt_payload, user_id):
    user = db.session.query(User).filter(User.id == user_id).first()

    if user is None:
        return jsonify({
            'success': False,
            'user': None,
            'msg': 'No user exists with id %s.' % user_id,
        }), HTTPStatus.BAD_REQUEST

    return jsonify({
        'success': True,
        'user': user_schema.dump(user).data,
        'msg': 'Successfully found user with id %s.' % user_id,
    }), HTTPStatus.OK

@user.route('/login', methods=['POST'])
def login():
    login_credentials, errors = validate_request(request, user_login_request_schema)
    if errors:
        return jsonify({
            'success': False,
            'msg': 'Request parameters are invalid',
            'error': errors
        }), HTTPStatus.BAD_REQUEST

    user = db.session.query(User).filter(User.username == login_credentials['username']).first()

    if user is None:
        return jsonify({
            'success': False,
            'msg': 'User does not exist for username "%s".' % login_credentials['username'],
        }), HTTPStatus.UNAUTHORIZED

    # Verify password
    valid_password = user.verify_password(login_credentials['password'])
    if not valid_password:
        return jsonify({
            'success': False,
            'msg': 'Invalid credentials',
        }), HTTPStatus.UNAUTHORIZED

    # Create JWT
    encoded_jwt = jwt.encode({
        'id': user.id
    }, 'secret', algorithm='HS256').decode("utf-8")

    user_data = user_schema.dump(user).data
    user_data.pop('password', None)
    return jsonify({
        'success': True,
        'jwt': encoded_jwt,
        'user': user_data,
        'msg': 'Successfully logged in.',
    }), HTTPStatus.OK

flask_app.register_blueprint(user)
