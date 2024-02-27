from ..base_classes import BaseAuthRequest

from ...utils import uuid_from_username


__all__ = (
    'ProfileRequest',
    'ProfilesRequest',
)


class ProfileRequest(BaseAuthRequest):
    def __init__(self, profile: str):
        super().__init__("skyblock/profile", profile=profile)


class ProfilesRequest(BaseAuthRequest):
    def __init__(self, uuid: str):
        super().__init__("skyblock/profiles", uuid=uuid)

    @classmethod
    async def from_username(cls, username: str):
        return cls(uuid=await uuid_from_username(username))
