from flask import Blueprint, request
from app.utils.jwt_validator import login_required

user = Blueprint('user', __name__, url_prefix='/api/user')

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
