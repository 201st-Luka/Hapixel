from ..abc import BaseRequest


__all__ = (
    'QuestsRequest',
)


class QuestsRequest(BaseRequest):
    def __init__(self):
        super().__init__("resources/quests")
