from ..base_classes import BaseRequest


__all__ = (
    'ChallengesRequest',
)


class ChallengesRequest(BaseRequest):
    def __init__(self):
        super().__init__("resources/challenges")
