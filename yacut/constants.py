import re
from string import ascii_letters, digits


PATTERN_FOR_SHORT = re.compile(r"[A-Za-z0-9]*")
REQUIRED_ORIGINAL_FIELD = 'Обязательное поле'
ORIGINAL_LABEL = 'Оригинальная ссылка'
SHORT_LABEL = 'Вариант короткой ссылки'
INCORRECT_SHORT_NAME = 'Указано недопустимое имя для короткой ссылки'
SUBMIT_NAME = 'Укоротить ссылку'

SHORT_MAX_LENGTH = 16
LENGTH_FOR_CODE_GENERATE = 6
ORIGINAL_MAX_LENGTH = 2000

SHORT_LINK_EXISTS = 'Предложенный вариант короткой ссылки уже существует.'
SHORT_LINK_CATEGORY = 'link-exists'

SHORT_ID_NOT_EXISTS = 'Указанный id не найден'
EMPTY_BODY = 'Отсутствует тело запроса'
REQUIRED_URL_FIELD = '"url" является обязательным полем!'

LETTERS_FOR_CODE = ascii_letters + digits

URL_MAP_VIEW_NAME = 'url_map_view'
