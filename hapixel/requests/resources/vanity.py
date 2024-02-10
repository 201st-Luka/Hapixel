from ..abc import BaseRequest


class VanityPetsRequest(BaseRequest):
    def __init__(self):
        super().__init__("vanity/pets")


class VanityCompanionsRequest(BaseRequest):
    def __init__(self):
        super().__init__("vanity/companions")
