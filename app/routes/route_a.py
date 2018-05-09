from flask import Blueprint, request

route_a = Blueprint('a', __name__, url_prefix='/api/a')

@route_a.route('/test1', methods=['GET', 'POST'])
def test1():
    if request.method == 'GET':
        return "A - Test1 - GET"
    else:
        return "A - Test1 - POST"

@route_a.route('/test2/<param>')
def test2(param):
    return "A - Test2 - GET - " + param
