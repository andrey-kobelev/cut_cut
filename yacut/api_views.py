from http import HTTPStatus

from flask import jsonify, request

from . import app
from .models import URLMap


@app.route('/api/id/<path:short>/', methods=['GET'])
def get_original(short):
    original = URLMap.get_url(short=short, api=True)
    return jsonify({'url': original.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def create_short():
    url_map = URLMap.add_url(
        data=request.get_json() if request.data else dict(),
        api=True
    )
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED
