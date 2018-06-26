from functools import wraps
from flask import request, jsonify
from http import HTTPStatus

import jwt

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        error = None
        message = ''

        if 'Authorization' in request.headers and 'Bearer' in request.headers['Authorization']:
            decodedJwt = {}
            encodedJwt = request.headers['Authorization'].replace('Bearer', '').strip()

            try:
                decodedJwt = jwt.decode(encodedJwt, 'secret', algorithms=['HS256'])
            except Exception:
                error = HTTPStatus.UNAUTHORIZED
                message = 'Unable to decode JWT successfully'

        else:
            error = HTTPStatus.UNAUTHORIZED
            message = 'Authorization missing from request header.'


        if error:
            return jsonify({
                'msg': message,
            }), error

        return f(decodedJwt, *args, **kwargs)
    return decorated_function
