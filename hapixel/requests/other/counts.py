from ..base_classes import BaseAuthRequest

from ...models import CountsGames


__all__ = (
    'CountsRequest',
)


class CountsRequest(BaseAuthRequest):
    def __init__(self):
        super().__init__("counts")

    games: CountsGames
    player_count: int
