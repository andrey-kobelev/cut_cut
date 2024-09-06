import random
import re
from datetime import datetime

from flask import url_for
from werkzeug.exceptions import NotFound

from yacut import db
from .constants import (
    PATTERN_FOR_SHORT,
    LETTERS_FOR_SHORT,
    LENGTH_FOR_SHORT_GENERATE,
    SHORT_MAX_LENGTH,
    ORIGINAL_MAX_LENGTH,
    URL_MAP_VIEW_NAME,
    NUM_ITERATIONS_FOR_FIND_UNIQUE_SHORT
)
from .exceptions import IncorrectShort, ShortExists


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
    def get_url_map(short, not_found_exception=False):
        url_map = URLMap.query.filter_by(short=short).first()
        if not_found_exception and url_map is None:
            raise NotFound()
        return url_map

    @staticmethod
    def get_short():
        for _ in range(NUM_ITERATIONS_FOR_FIND_UNIQUE_SHORT):
            short = ''.join(random.choices(
                population=LETTERS_FOR_SHORT,
                k=LENGTH_FOR_SHORT_GENERATE
            ))
            if URLMap.get_url_map(short) is None:
                return short

    @staticmethod
    def add_url(original, short, incorrect_short_error=False):
        if short:
            if incorrect_short_error:
                if (
                    len(short) > SHORT_MAX_LENGTH
                    or not re.fullmatch(PATTERN_FOR_SHORT, short)
                ):
                    raise IncorrectShort()
            if URLMap.get_url_map(short) is not None:
                raise ShortExists()
        else:
            short = URLMap.get_short()
        url_map = URLMap(original=original, short=short)
        db.session.add(url_map)
        db.session.commit()
        return url_map
