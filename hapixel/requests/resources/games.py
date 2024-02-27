from ..base_classes import BaseRequest


__all__ = (
    'GamesRequest',
)


class GamesRequest(BaseRequest):
    def __init__(self):
        super().__init__("resources/games")
