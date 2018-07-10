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

@user.route('', methods=['GET'])
@login_required
def getUser(user):
    print(user)
    user = db.session.query(User).filter(User.id == user['id']).first()

    if user is None:
        return jsonify({
            'user': None,
            'success': True,
            'msg': 'No user exists with id %s.' % user_id,
        }), HTTPStatus.OK

    return jsonify({
        'user': user_schema.dump(user).data,
        'success': True,
        'msg': 'Successfully found user with id %s.' % user_id,
    }), HTTPStatus.OK

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

@user.route('/<user_id>', methods=['GET'])
@login_required
def test2(user, user_id):
    user = db.session.query(User).filter(User.id == user_id).first()

    if user is None:
        return jsonify({
            'user': None,
            'success': True,
            'msg': 'No user exists with id %s.' % user_id,
        }), HTTPStatus.OK

    return jsonify({
        'user': user_schema.dump(user).data,
        'success': True,
        'msg': 'Successfully found user with id %s.' % user_id,
    }), HTTPStatus.OK

flask_app.register_blueprint(user)
