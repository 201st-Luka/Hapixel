from ..base_classes import BaseAuthRequest
from ...utils import uuid_from_username


__all__ = (
    'RecentGamesRequest',
)


class RecentGamesRequest(BaseAuthRequest):
    def __init__(self, player_uuid: str):
        super().__init__("recentgames", uuid=player_uuid)

    @classmethod
    async def from_username(cls, username: str) -> 'RecentGamesRequest':
        return cls(await uuid_from_username(username))
