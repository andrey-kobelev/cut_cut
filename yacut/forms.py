from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional



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
            DataRequired(message='Обязательное поле'),
            Length(1, 16),
            Optional()
        ]
    )
    submit = SubmitField('Укоротить ссылку')
