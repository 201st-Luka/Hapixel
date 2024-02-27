from .base_classes import BaseResponse, FieldFormatter


__all__ = (
    'Booster',
    'BoosterState',
)


class Booster(BaseResponse):
    id: str = FieldFormatter('_id')
    purchaser_uuid: str
    amount: float
    original_length: int
    length: int
    game_type: int
    date_activated: int
    stacked: list[str]


class BoosterState(BaseResponse):
    decrementing: bool
