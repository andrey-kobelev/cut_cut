from http import HTTPStatus

from flask import jsonify, request

from . import app
from .constants import (
    EMPTY_BODY,
    REQUIRED_URL_FIELD,
    SHORT_NOT_EXISTS
)
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/<path:short>/', methods=['GET'])
def get_original(short):
    url_map = URLMap.get_url_map(short=short)
    if not url_map:
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
        return jsonify(
            URLMap.add_url(
                original=data['url'],
                short=data.get('custom_id', ''),
                validation=True
            ).to_dict()
        ), HTTPStatus.CREATED
    except (
        URLMap.IncorrectShort,
        URLMap.ShortExists,
        URLMap.BadURLLength,
        URLMap.FailGenerateShort
    ) as error:
        raise InvalidAPIUsage(str(error))
