import random

from .constants import LENGTH_FOR_CODE_GENERATE, LETTERS_FOR_CODE


class URLEncoder:

    def __init__(self, model, original_url=None):
        self.url = original_url
        self.model = model

    @classmethod
    def get_code(cls, url):
        return ''.join(random.choices(
            population=LETTERS_FOR_CODE,
            k=LENGTH_FOR_CODE_GENERATE
        ))

    def encode(self):
        short_url = self.get_code(self.url)
        while self.model.query.filter_by(short=short_url).first() is not None:
            short_url = self.get_code(self.url)
        return short_url
