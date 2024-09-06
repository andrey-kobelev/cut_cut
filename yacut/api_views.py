from http import HTTPStatus

from flask import jsonify, request
from werkzeug.exceptions import NotFound

from . import app
from .constants import (
    EMPTY_BODY,
    REQUIRED_URL_FIELD,
    INCORRECT_SHORT_NAME,
    SHORT_EXISTS, SHORT_NOT_EXISTS
)
from .error_handlers import InvalidAPIUsage
from .exceptions import IncorrectShort, ShortExists
from .models import URLMap


@app.route('/api/id/<path:short>/', methods=['GET'])
def get_original(short):
    try:
        url_map = URLMap.get_url_map(short=short, not_found_exception=True)
    except NotFound:
        raise InvalidAPIUsage(
            SHORT_NOT_EXISTS, HTTPStatus.NOT_FOUND
        )
    return jsonify(
        {'url': url_map.original}
    ), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def create_short():
    if not request.data:
        raise InvalidAPIUsage(EMPTY_BODY)
    data = request.get_json()
    if 'url' not in data:
        raise InvalidAPIUsage(REQUIRED_URL_FIELD)
    try:
        short = data['custom_id']
    except KeyError:
        short = ''

    try:
        url_map = URLMap.add_url(
            original=data['url'],
            short=short,
            incorrect_short_error=True
        )
    except IncorrectShort:
        raise InvalidAPIUsage(INCORRECT_SHORT_NAME)
    except ShortExists:
        raise InvalidAPIUsage(SHORT_EXISTS)

    return jsonify(
        url_map.to_dict()
    ), HTTPStatus.CREATED
