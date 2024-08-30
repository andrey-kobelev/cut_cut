import re

PATTERN_FOR_SHORT = re.compile(r"[A-Za-z0-9]{0,16}")
REQUIRED_ORIGINAL_FIELD = 'Обязательное поле'
ORIGINAL_LABEL = 'Оригинальная ссылка'
SHORT_LABEL = 'Вариант короткой ссылки'
INCORRECT_SHORT_NAME = 'Указано недопустимое имя для короткой ссылки'
SUBMIT_NAME = 'Укоротить ссылку'

MIN_SHORT_LENGTH = 0
MAX_SHORT_LENGTH = 16

SHORT_LINK_EXISTS = 'Предложенный вариант короткой ссылки уже существует.'
SHORT_LINK_CATEGORY = 'link-exists'

SHORT_ID_NOT_EXISTS = 'Указанный id не найден'
EMPTY_BODY = 'Отсутствует тело запроса'
REQUIRED_URL_FIELD = '"url" является обязательным полем!'

LETTERS_FOR_CODE = (
    'zxcvbnmasdfghjklqwertyui'
    'QWERTYUASDFGHJKLZXCVBNM'
    '1234567890'
)
LENGTH_FOR_CODE_GENERATE = 6