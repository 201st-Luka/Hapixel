from ..abc import BaseRequest

__all__ = (
    'CollectionsRequest',
)


class CollectionsRequest(BaseRequest):
    def __init__(self):
        super().__init__("resources/skyblock/collections")
