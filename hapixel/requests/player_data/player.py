from ..base_classes import BaseAuthRequest
from ...utils import uuid_from_username, UUID


__all__ = (
    'PlayerRequest',
)


class PlayerRequest(BaseAuthRequest):
    def __init__(self, player_uuid: UUID):
        super().__init__("player", uuid=player_uuid)

    @classmethod
    async def from_username(cls, username: str) -> 'PlayerRequest':
        return cls(await uuid_from_username(username))
