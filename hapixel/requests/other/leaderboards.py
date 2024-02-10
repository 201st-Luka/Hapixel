from ..abc import BaseAuthRequest


__all__ = (
    'LeaderboardsRequest',
)


class LeaderboardsRequest(BaseAuthRequest):
    def __init__(self):
        super().__init__("leaderboards")
