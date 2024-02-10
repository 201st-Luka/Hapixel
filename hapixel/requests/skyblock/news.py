from ..abc import BaseAuthRequest


__all__ = (
    'NewsRequest',
)


class NewsRequest(BaseAuthRequest):
    def __init__(self):
        super().__init__("skyblock/news")
