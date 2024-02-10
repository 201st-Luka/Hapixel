from asyncio import Future


class RequestItem:
    def __init__(
            self,
            url: str,
            params: dict | None,
    ):
        self.url = url
        self.params = params

        self.future: Future = Future()

    def __repr__(self) -> str:
        return f"<RequestItem url={self.url}, params={self.params}>"
