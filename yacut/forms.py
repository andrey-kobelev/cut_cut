import re

from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp


pattern = re.compile(r"(?P<head>https?://\w{1,16})")

class CutURLForm(FlaskForm):
    original_link = URLField(
        'Оригинальная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
        ]
    )
    custom_id = URLField(
        'Вариант короткой ссылки',
        validators=[
            Length(0, 16),
            Regexp(regex=pattern, message='Недопустимые символы для ссылки'),
            Optional()
        ]
    )
    submit = SubmitField('Укоротить ссылку')
