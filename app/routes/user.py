import datetime
from flask import Blueprint, request, jsonify
from http import HTTPStatus
from sqlalchemy import exc
from app.models import db
from app.models.user import User
from app.utils.jwt_validator import login_required

user = Blueprint('user', __name__, url_prefix='/api/user')

# login
@user.route('/register', methods=['POST'])
def register():
    # validate body

    # create user
    try:
        user = User(
            email=request.json['email'],
            password=request.json['password'],
            username=request.json['username'],
            first_name=request.json['first_name'],
            last_name=request.json['last_name'],
            birthday=datetime.date(1994, 9, 21),
            city=request.json['city'],
            country=request.json['country']
        )
    except exc.IntegrityError:
        return jsonify({
            'success': False,
            'msg': 'Account already exists for this email.',
        }), HTTPStatus.OK

    db.session.add(user)
    db.session.commit()

    return jsonify({
        'user': dict(user),
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
