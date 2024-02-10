from ..abc import BaseAuthRequest
from ...collections import HapixelException
from ...utils import uuid_from_username


__all__ = (
    'GuildRequest',
)


class GuildRequest(BaseAuthRequest):
    def __init__(self, id_: str = None, player_uuid: str = None, name: str = None):
        if id_ is None and player_uuid is None and name is None:
            raise HapixelException("At least one parameter has to be different from 'None'")
        super().__init__("guild", id=id_, player=player_uuid, name=name)

    @classmethod
    async def from_username(cls, username: str, id_: str = None, name: str = None):
        return cls(id_, await uuid_from_username(username), name)
