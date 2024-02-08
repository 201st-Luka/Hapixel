from ..abc import BaseRequest
from ...utils import uuid_from_username


__all__ = (
    'PlayerRequest',
)


class PlayerRequest(BaseRequest):
    def __init__(self, uuid: str):
        super().__init__("player", uuid=uuid)

    @classmethod
    async def from_username(cls, username: str) -> 'PlayerRequest':
        return cls(await uuid_from_username(username))
