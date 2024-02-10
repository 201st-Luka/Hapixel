from ..abc import BaseRequest, BaseAuthRequest

from ...utils import uuid_from_username


__all__ = (
    'BingoGoalsRequest',
    'BingoDataRequest',
)


class BingoGoalsRequest(BaseRequest):
    def __init__(self):
        super().__init__("resources/skyblock/bingo")


class BingoDataRequest(BaseAuthRequest):
    def __init__(self, uuid: str):
        super().__init__("skyblock/bingo", uuid=uuid)

    @classmethod
    async def from_username(cls, username: str):
        return cls(uuid=await uuid_from_username(username))
