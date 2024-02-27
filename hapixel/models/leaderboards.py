from typing import Iterator

from ..collections import Games
from .base_classes import BaseEnumGetter, BaseResponse, BaseIterator, FieldFormatter, Factory
from ..utils import UUID


class Leaderboard(BaseResponse):
    path: str
    prefix: str
    title: str
    location: str
    count: int
    leaders: BaseIterator[UUID] = FieldFormatter("leaders", BaseIterator, UUID)


class Leaderboards(BaseEnumGetter):
    _factory = Factory(BaseIterator[Leaderboard], Leaderboard)

    def get_value(self, enum: Games) -> BaseIterator[Leaderboard]:
        return BaseIterator(super().get_value(enum), Leaderboard)
