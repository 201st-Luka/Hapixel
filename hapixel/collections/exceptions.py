class HapixelException(Exception):
    pass


class ApiKeyException(HapixelException):
    pass


class RequestNotDone(HapixelException):
    def __str__(self) -> str:
        return "The request has not been done yet"


class NoAuthenticationProvided(HapixelException):
    def __str__(self) -> str:
        return "No authentication has been provided, add an API key to the client to make authenticated requests"
