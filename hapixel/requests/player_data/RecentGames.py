from ..abc import BaseRequest
from ...utils import uuid_from_username


__all__ = (
    'RecentGamesRequest',
)


class RecentGamesRequest(BaseRequest):
    def __init__(self, uuid: str):
        super().__init__("recentgames", uuid=uuid)

    @classmethod
    async def from_username(cls, username: str) -> 'RecentGamesRequest':
        return cls(await uuid_from_username(username))
