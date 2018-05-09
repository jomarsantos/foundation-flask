from flask import Blueprint, request

module_a = Blueprint('module_a', __name__, url_prefix='/api/module_a')

@module_a.route('/test1', methods=['GET', 'POST'])
def test1():
    if request.method == 'GET':
        return "Module A - Test1 - GET"
    else:
        return "Module A - Test1 - POST"

@module_a.route('/test2/<param>')
def test2(param):
    return "Module A - Tes21 - GET - " + param
