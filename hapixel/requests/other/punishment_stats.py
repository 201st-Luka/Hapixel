from ..abc import BaseAuthRequest


__all__ = (
    'PunishmentStatsRequest',
)


class PunishmentStatsRequest(BaseAuthRequest):
    def __init__(self):
        super().__init__("punishmentstats")
