import json

def validate_request(request, schema):
    request_params = {}

    for key, value in request.get_json().items():
        if value.strip():
            request_params[key] = value
        else:
            request_params[key] = None

    return schema.load(request_params)
