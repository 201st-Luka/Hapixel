from ..base_classes import BaseAuthRequest
from ...models import FieldFormatter


__all__ = (
    'PunishmentStatsRequest',
)


class PunishmentStatsRequest(BaseAuthRequest):
    def __init__(self):
        super().__init__("punishmentstats")

    watchdog_last_minute: int = FieldFormatter("watchdog_lastMinute", int)
    staff_rolling_daily: int = FieldFormatter("staff_rollingDaily", int)
    watchdog_total: int = FieldFormatter("watchdog_total", int)
    watchdog_rolling_daily: int = FieldFormatter("watchdog_rollingDaily", int)
    staff_total: int = FieldFormatter("staff_total", int)
