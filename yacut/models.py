import random
import re
from datetime import datetime

from flask import url_for

from yacut import db
from .constants import (
    SHORT_PATTERN,
    SHORT_CHARACTERS,
    LENGTH_FOR_SHORT_GENERATE,
    SHORT_MAX_LENGTH,
    ORIGINAL_MAX_LENGTH,
    URL_MAP_VIEW_NAME,
    NUM_ITERATIONS_FOR_FIND_UNIQUE_SHORT,
    INCORRECT_SHORT_NAME,
    SHORT_EXISTS,
    BAD_ORIGINAL_LENGTH
)
from .exceptions import YaCutBaseException


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(ORIGINAL_MAX_LENGTH))
    short = db.Column(db.String(SHORT_MAX_LENGTH), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    class ShortExists(YaCutBaseException):
        pass

    class IncorrectShort(YaCutBaseException):
        pass

    class BadURLLength(YaCutBaseException):
        pass

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
    def get_url_map(short):
        return URLMap.query.filter_by(short=short).first()

    @staticmethod
    def generate_short():
        short = None
        for _ in range(NUM_ITERATIONS_FOR_FIND_UNIQUE_SHORT):
            short = ''.join(random.choices(
                population=SHORT_CHARACTERS,
                k=LENGTH_FOR_SHORT_GENERATE
            ))
            if not URLMap.get_url_map(short):
                break
        if not short:
            return URLMap.generate_short()
        return short

    @staticmethod
    def add_url(original, short):
        if short:
            if (
                len(short) > SHORT_MAX_LENGTH
                or not re.fullmatch(SHORT_PATTERN, short)
            ):
                raise URLMap.IncorrectShort(INCORRECT_SHORT_NAME)
            if URLMap.get_url_map(short):
                raise URLMap.ShortExists(SHORT_EXISTS)
        else:
            short = URLMap.generate_short()
        if len(original) > ORIGINAL_MAX_LENGTH:
            raise URLMap.BadURLLength(BAD_ORIGINAL_LENGTH)
        url_map = URLMap(original=original, short=short)
        db.session.add(url_map)
        db.session.commit()
        return url_map
