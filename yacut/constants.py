import re
from string import ascii_letters, digits

LETTERS_FOR_SHORT = ascii_letters + digits
PATTERN_FOR_SHORT = re.compile(f'[{LETTERS_FOR_SHORT}]*')
REQUIRED_ORIGINAL_FIELD = 'Обязательное поле'
ORIGINAL_LABEL = 'Оригинальная ссылка'
SHORT_LABEL = 'Вариант короткой ссылки'
INCORRECT_SHORT_NAME = 'Указано недопустимое имя для короткой ссылки'
SUBMIT_NAME = 'Укоротить ссылку'

SHORT_MAX_LENGTH = 16
LENGTH_FOR_SHORT_GENERATE = 6
ORIGINAL_MAX_LENGTH = 2000

SHORT_EXISTS = 'Предложенный вариант короткой ссылки уже существует.'

SHORT_NOT_EXISTS = 'Указанный id не найден'
EMPTY_BODY = 'Отсутствует тело запроса'
REQUIRED_URL_FIELD = '"url" является обязательным полем!'

URL_MAP_VIEW_NAME = 'url_map_view'

NUM_ITERATIONS_FOR_FIND_UNIQUE_SHORT = 10