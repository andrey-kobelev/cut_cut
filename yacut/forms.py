from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from .constants import (
    SHORT_PATTERN,
    ORIGINAL_LABEL,
    REQUIRED_ORIGINAL_FIELD,
    SHORT_LABEL,
    SHORT_MAX_LENGTH,
    INCORRECT_SHORT_NAME,
    SUBMIT_NAME,
    ORIGINAL_MAX_LENGTH
)


class CutURLForm(FlaskForm):
    original_link = URLField(
        ORIGINAL_LABEL,
        validators=[
            DataRequired(message=REQUIRED_ORIGINAL_FIELD),
            Length(max=ORIGINAL_MAX_LENGTH)
        ]
    )
    custom_id = URLField(
        SHORT_LABEL,
        validators=[
            Length(max=SHORT_MAX_LENGTH),
            Regexp(
                regex=SHORT_PATTERN,
                message=INCORRECT_SHORT_NAME
            ),
            Optional()
        ]
    )
    submit = SubmitField(SUBMIT_NAME)
