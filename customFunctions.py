from json import dumps
from flask import make_response


def jsonify(status=200, indent=2, sort_keys=True, **kwargs):
    response = make_response(
        dumps(dict(**kwargs), indent=indent, sort_keys=sort_keys))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['mimetype'] = 'application/json'
    response.status_code = status
    return response
