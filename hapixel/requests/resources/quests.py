from ..base_classes import BaseRequest


__all__ = (
    'QuestsRequest',
)


class QuestsRequest(BaseRequest):
    def __init__(self):
        super().__init__("resources/quests")
