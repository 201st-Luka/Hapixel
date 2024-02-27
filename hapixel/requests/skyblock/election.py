from ..base_classes import BaseRequest

__all__ = (
    'ElectionRequest',
)


class ElectionRequest(BaseRequest):
    def __init__(self):
        super().__init__("resources/skyblock/election")
