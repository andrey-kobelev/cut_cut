from http import HTTPStatus


class YaCutBaseException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message


class InvalidAPIUsage(YaCutBaseException):
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, message, status_code=None):
        super().__init__(message)
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)
