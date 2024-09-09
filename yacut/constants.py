import re
from string import ascii_letters, digits

SHORT_CHARACTERS = ascii_letters + digits
SHORT_PATTERN = re.compile(f'[{SHORT_CHARACTERS}]*')
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

BAD_ORIGINAL_LENGTH = 'Длина оригинальной ссылки превышает норму'

NUM_ITERATIONS_FOR_FIND_UNIQUE_SHORT = 10
