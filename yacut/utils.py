import random
import re


class URLEncoder:
    pattern = re.compile(r"(?P<head>https?://[\w.-]+/)")

    def __init__(self, model, original_url=None, short_url=None):
        self.short_url = short_url
        self.url = original_url
        self.model = model

    @classmethod
    def get_code(cls):
        return ''.join(random.choices(
            population=(
                'zxcvbnmasdfghjklqwertyui'
                'QWERTYUASDFGHJKLZXCVBNM'
                '1234567890'
            ),
            k=4
        ))

    def encode(self):
        head = re.search(self.pattern, self.url).group('head')
        short_url = f'{head}{self.get_code()}'
        while self.model.query.filter_by(short=short_url).first() is not None:
            short_url = f'{head}{self.get_code()}'
        return short_url

    def decode(self):
        return self.model.query.get(short=self.short_url).original
