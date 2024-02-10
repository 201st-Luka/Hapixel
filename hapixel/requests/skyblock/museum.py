from ..abc import BaseAuthRequest


__all__ = (
    'MuseumRequest',
)


class MuseumRequest(BaseAuthRequest):
    def __init__(self, profile: str):
        super().__init__("skyblock/museum", profile=profile)
