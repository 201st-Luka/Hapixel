from ..base_classes import BaseRequest


__all__ = (
    'VanityPetsRequest',
    'VanityCompanionsRequest',
)


class VanityPetsRequest(BaseRequest):
    def __init__(self):
        super().__init__("resources/vanity/pets")


class VanityCompanionsRequest(BaseRequest):
    def __init__(self):
        super().__init__("resources/vanity/companions")
