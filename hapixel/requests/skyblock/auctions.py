from ..base_classes import BaseAuthRequest, BaseRequest

from ...utils import uuid_from_username


__all__ = (
    'AuctionRequest',
    'AuctionsRequest',
    'EndedAuctionsRequest',
)


class AuctionRequest(BaseAuthRequest):
    def __init__(self, uuid: str = None, player: str = None, profile: str = None):
        if sum([bool(uuid), bool(player), bool(profile)]) != 1:
            raise ValueError("You must provide either a uuid, player or profile")

        super().__init__("skyblock/auction", uuid=uuid, player=player, profile=profile)

    @classmethod
    def from_uuid(cls, uuid: str):
        return cls(uuid=uuid)

    @classmethod
    def from_player(cls, player: str):
        return cls(player=player)

    @classmethod
    async def from_username(cls, username: str):
        return cls(player=await uuid_from_username(username))

    @classmethod
    def from_profile(cls, profile: str):
        return cls(profile=profile)


class AuctionsRequest(BaseRequest):
    def __init__(self, page: int = 0):
        super().__init__("skyblock/auctions", page=page)


class EndedAuctionsRequest(BaseRequest):
    def __init__(self):
        super().__init__("skyblock/auctions_ended")
