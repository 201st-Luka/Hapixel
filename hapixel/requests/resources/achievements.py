from ..abc import BaseRequest


__all__ = (
    'AchievementsRequest',
)


class AchievementsRequest(BaseRequest):
    def __init__(self):
        super().__init__("resources/achievements")
