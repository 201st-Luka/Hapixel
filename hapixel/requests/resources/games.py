from ..abc import BaseRequest


class GamesRequest(BaseRequest):
    def __init__(self):
        super().__init__("games")
