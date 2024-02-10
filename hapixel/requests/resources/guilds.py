from ..abc import BaseRequest


class GuildAchievementsRequest(BaseRequest):
    def __init__(self):
        super().__init__("guilds/achievements")
