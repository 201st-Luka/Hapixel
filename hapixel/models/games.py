from .base_classes import BaseEnumGetter, BaseResponse, Factory
from ..collections import Games, Servers


class CountsGameModes(BaseResponse):
    players: int
    modes: dict[str, int]


class CountsGames(BaseEnumGetter):
    _factory = Factory(CountsGameModes)

    def get_value(self, enum: Games | Servers) -> CountsGameModes:
        return super().get_value(enum)
