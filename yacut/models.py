import random
import re
from datetime import datetime
from http import HTTPStatus

from flask import url_for, abort

from yacut import db
from .constants import (
    EMPTY_BODY,
    REQUIRED_URL_FIELD,
    PATTERN_FOR_SHORT,
    INCORRECT_SHORT_NAME,
    LETTERS_FOR_CODE,
    LENGTH_FOR_CODE_GENERATE,
    SHORT_LINK_EXISTS,
    SHORT_ID_NOT_EXISTS,
    SHORT_MAX_LENGTH,
    ORIGINAL_MAX_LENGTH,
    URL_MAP_VIEW_NAME
)
from .error_handlers import InvalidAPIUsage


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(ORIGINAL_MAX_LENGTH))
    short = db.Column(db.String(SHORT_MAX_LENGTH), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                endpoint=URL_MAP_VIEW_NAME,
                short=self.short,
                _external=True
            ),
        )

    @staticmethod
    def is_short_exists(short):
        return URLMap.query.filter_by(short=short).first() is not None

    @staticmethod
    def get_code():
        return ''.join(random.choices(
            population=LETTERS_FOR_CODE,
            k=LENGTH_FOR_CODE_GENERATE
        ))

    @staticmethod
    def encode(get_code):
        short = get_code()
        while URLMap.is_short_exists(short):
            short = get_code()
        return short

    @staticmethod
    def add_url(data, api=False):
        if api:
            if not data:
                raise InvalidAPIUsage(EMPTY_BODY)
            if 'url' not in data:
                raise InvalidAPIUsage(REQUIRED_URL_FIELD)
            if 'custom_id' in data:
                short = data['custom_id']
                if (
                    not re.fullmatch(PATTERN_FOR_SHORT, short)
                    or len(short) > SHORT_MAX_LENGTH
                ):
                    raise InvalidAPIUsage(INCORRECT_SHORT_NAME)
                if URLMap.is_short_exists(short):
                    raise InvalidAPIUsage(
                        SHORT_LINK_EXISTS
                    )
        if 'custom_id' not in data or not data['custom_id']:
            short = URLMap.encode(URLMap.get_code)
        else:
            short = data['custom_id']
        original = data[
            'original_link'
        ] if 'original_link' in data else data['url']
        url_map = URLMap(original=original, short=short)
        db.session.add(url_map)
        db.session.commit()
        return url_map

    @staticmethod
    def get_url(short, api=False):
        url = URLMap.query.filter_by(short=short).first()
        if url is None:
            if api:
                raise InvalidAPIUsage(
                    SHORT_ID_NOT_EXISTS, HTTPStatus.NOT_FOUND
                )
            else:
                abort(HTTPStatus.NOT_FOUND)
        return url
