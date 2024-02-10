from ..abc import BaseAuthRequest


__all__ = (
    'BoostersRequest',
)


class BoostersRequest(BaseAuthRequest):
    def __init__(self):
        super().__init__("boosters")
