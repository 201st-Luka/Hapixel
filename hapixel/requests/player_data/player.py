from ..abc import BaseAuthRequest
from ...utils import uuid_from_username


__all__ = (
    'PlayerRequest',
)


class PlayerRequest(BaseAuthRequest):
    def __init__(self, player_uuid: str):
        super().__init__("player", uuid=player_uuid)

    @classmethod
    async def from_username(cls, username: str) -> 'PlayerRequest':
        return cls(await uuid_from_username(username))
