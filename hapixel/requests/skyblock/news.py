from ..base_classes import BaseAuthRequest


__all__ = (
    'NewsRequest',
)


class NewsRequest(BaseAuthRequest):
    def __init__(self):
        super().__init__("skyblock/news")
