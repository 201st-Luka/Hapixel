from .base_classes import BaseResponse


class Rank(BaseResponse):
    name: str
    default: bool
    tag: str
    created: int
    priority: int
