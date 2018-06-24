from app.main import flask_app
from http import HTTPStatus

# HANDLE INVALID ROUTES
@flask_app.errorhandler(HTTPStatus.NOT_FOUND.value)
def page_not_found(e):
    return jsonify({
        'msg': 'This endpoint does not exist.',
    }), HTTPStatus.NOT_FOUND

# INVALID METHODS
@flask_app.errorhandler(HTTPStatus.METHOD_NOT_ALLOWED.value)
def method_not_allowed(e):
    return jsonify({
        'msg': 'This endpoint does not support this method.'
    }), HTTPStatus.METHOD_NOT_ALLOWED

# SERVER ERRORS
@flask_app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR.value)
def internal_server_error(e):
    return jsonify({
        'msg': 'Internal server error.',
    }), HTTPStatus.INTERNAL_SERVER_ERROR
