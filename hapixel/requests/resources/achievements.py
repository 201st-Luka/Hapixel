from ..abc import BaseRequest


class AchievementsRequest(BaseRequest):
    def __init__(self):
        super().__init__("achievements")
