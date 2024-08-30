from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from .constants import (
    PATTERN_FOR_SHORT,
    ORIGINAL_LABEL,
    REQUIRED_ORIGINAL_FIELD,
    SHORT_LABEL,
    MIN_SHORT_LENGTH,
    MAX_SHORT_LENGTH,
    INCORRECT_SHORT_NAME,
    SUBMIT_NAME
)


class CutURLForm(FlaskForm):
    original_link = URLField(
        ORIGINAL_LABEL,
        validators=[
            DataRequired(message=REQUIRED_ORIGINAL_FIELD),
        ]
    )
    custom_id = URLField(
        SHORT_LABEL,
        validators=[
            Length(MIN_SHORT_LENGTH, MAX_SHORT_LENGTH),
            Regexp(
                regex=PATTERN_FOR_SHORT,
                message=INCORRECT_SHORT_NAME
            ),
            Optional()
        ]
    )
    submit = SubmitField(SUBMIT_NAME)
