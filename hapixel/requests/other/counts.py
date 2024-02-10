from ..abc import BaseAuthRequest


__all__ = (
    'CountsRequest',
)


class CountsRequest(BaseAuthRequest):
    def __init__(self):
        super().__init__("counts")
