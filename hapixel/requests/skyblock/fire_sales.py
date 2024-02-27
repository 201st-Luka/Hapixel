from ..base_classes import BaseRequest


__all__ = (
    'FireSalesRequest',
)


class FireSalesRequest(BaseRequest):
    def __init__(self):
        super().__init__("skyblock/firesales")
