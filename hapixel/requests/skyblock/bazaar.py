from ..base_classes import BaseRequest


__all__ = (
    'BazaarRequest',
)


class BazaarRequest(BaseRequest):
    def __init__(self):
        super().__init__("skyblock/bazaar")
