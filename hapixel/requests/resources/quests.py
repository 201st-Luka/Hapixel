from ..abc import BaseRequest


class QuestsRequest(BaseRequest):
    def __init__(self):
        super().__init__("quests")
