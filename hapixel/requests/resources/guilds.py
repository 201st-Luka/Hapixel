from ..abc import BaseRequest


__all__ = (
    'GuildAchievementsRequest',
)


class GuildAchievementsRequest(BaseRequest):
    def __init__(self):
        super().__init__("resources/guilds/achievements")
