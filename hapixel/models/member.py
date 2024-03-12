from .base_classes import BaseResponse
from ..utils import UUID


__all__ = (
    'Member',
)


class Member(BaseResponse):
    uuid: UUID
    rank: str
    joined: int
    quest_participation: int
    muted_till: int
    expHistory: dict
