from ..base_classes import BaseAuthRequest

from ...models import BoosterState, BaseIterator, Booster, FieldFormatter


__all__ = (
    'BoostersRequest',
)


class BoostersRequest(BaseAuthRequest):
    def __init__(self):
        super().__init__("boosters")

    boosters: BaseIterator[Booster] = FieldFormatter(sub_type=Booster)
    booster_state: BoosterState
