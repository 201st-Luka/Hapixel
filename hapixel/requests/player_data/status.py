from ..base_classes import BaseAuthRequest
from ...utils import uuid_from_username


__all__ = (
    'StatusRequest',
)


class StatusRequest(BaseAuthRequest):
    def __init__(self, player_uuid: str):
        super().__init__("status", uuid=player_uuid)

    @classmethod
    async def from_username(cls, username: str) -> 'StatusRequest':
        return cls(await uuid_from_username(username))
