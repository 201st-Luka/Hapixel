from ..base_classes import BaseAuthRequest
from ...models import Leaderboards

__all__ = (
    'LeaderboardsRequest',
)


class LeaderboardsRequest(BaseAuthRequest):
    def __init__(self):
        super().__init__("leaderboards")

    leaderboards: Leaderboards
