from ..abc import BaseRequest


__all__ = (
    'SkillsRequest',
)


class SkillsRequest(BaseRequest):
    def __init__(self):
        super().__init__("resources/skyblock/skills")
