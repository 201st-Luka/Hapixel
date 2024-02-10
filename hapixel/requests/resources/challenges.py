from ..abc import BaseRequest


class ChallengesRequest(BaseRequest):
    def __init__(self):
        super().__init__("challenges")
