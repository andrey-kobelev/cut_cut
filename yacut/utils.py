import random
import re


class URLEncoder:
    pattern = re.compile(r"(?P<head>https?://)")

    def __init__(self, model, original_url=None):
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
            k=8
        ))

    def encode(self):
        head = re.search(self.pattern, self.url).group('head')
        short_url = f'{head}{self.get_code()}'
        while self.model.query.filter_by(short=short_url).first() is not None:
            short_url = f'{head}{self.get_code()}'
        return short_url
