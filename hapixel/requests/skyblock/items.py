from ..base_classes import BaseRequest


__all__ = (
    'ItemsRequest',
)


class ItemsRequest(BaseRequest):
    def __init__(self):
        super().__init__("resources/skyblock/items")
