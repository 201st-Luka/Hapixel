class HapixelException(Exception):
    pass


class ApiKeyException(HapixelException):
    pass


class RequestNotDone(HapixelException):
    def __str__(self) -> str:
        return "The request has not been done yet"
