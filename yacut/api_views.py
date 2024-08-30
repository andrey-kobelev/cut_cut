import re

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .forms import PATTERN_FOR_SHORT
from .utils import URLEncoder
from .constants import (
    SHORT_ID_NOT_EXISTS,
    EMPTY_BODY,
    REQUIRED_URL_FIELD,
    INCORRECT_SHORT_NAME,
    SHORT_LINK_EXISTS
)


@app.route('/api/id/<path:short_id>/', methods=['GET'])
def get_original(short_id):
    original = URLMap.query.filter_by(short=short_id).first()
    if original is None:
        raise InvalidAPIUsage(SHORT_ID_NOT_EXISTS, 404)
    return jsonify({'url': original.original}), 200


@app.route('/api/id/', methods=['POST'])
def create_short():
    if not request.data:
        raise InvalidAPIUsage(EMPTY_BODY)
    data = request.get_json()
    custom_id = data.get('custom_id', None)
    url = data.get('url', None)
    if not url:
        raise InvalidAPIUsage(REQUIRED_URL_FIELD)
    if custom_id and not re.fullmatch(PATTERN_FOR_SHORT, custom_id):
        raise InvalidAPIUsage(INCORRECT_SHORT_NAME)
    if (
        custom_id
        and URLMap.query.filter_by(short=custom_id).first() is not None
    ):
        raise InvalidAPIUsage(
            SHORT_LINK_EXISTS
        )
    if not custom_id:
        custom_id = URLEncoder(model=URLMap, original_url=url).encode()
    url_map = URLMap(original=url, short=custom_id)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), 201
