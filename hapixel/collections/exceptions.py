class HapixelException(Exception):
    pass


class RequestNotDone(HapixelException):
    def __str__(self) -> str:
        return "The request has not been done yet"


class NoAuthenticationProvided(HapixelException):
    def __str__(self) -> str:
        return "No authentication has been provided, add an API key to the client to make authenticated requests"


class ApiException(HapixelException):
    def __init__(self, *args, cause: str = None):
        if not args:
            super().__init__(f"An API exception occurred.")
        else:
            super().__init__(*args)
        self.cause = cause

    def __str__(self) -> str:
        if self.cause is not None:
            return super().__str__() + f"\ncause: '{self.cause}'"
        return super().__str__()


class ApiKeyException(ApiException):
    pass


class MissingData(ApiException):
    pass


class NoData(ApiException):
    pass


class InvalidData(ApiException):
    pass


class Forbidden(ApiException):
    pass


class Throttled(ApiException):
    def __init__(self, *args, cause: str = None, throttle: bool = None, global_: bool = None):
        super().__init__(*args)
        self.cause = cause
        self.throttle = throttle
        self.global_ = global_

    def __str__(self) -> str:
        string = super().__str__()

        if self.cause is not None:
            string += f"\ncause: '{self.cause}'"
        if self.throttle is not None:
            string += f"\nthrottle: '{self.throttle}'"
        if self.global_ is not None:
            string += f"\nglobal: '{self.global_}'"

        return string


class UnavailableData(ApiException):
    pass
