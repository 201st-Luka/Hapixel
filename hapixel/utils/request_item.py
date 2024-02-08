from asyncio import Future


class RequestItem:
    def __init__(
            self,
            url: str,
            data: dict | None,
    ):
        self.url = url
        self.data = data

        self.future: Future = Future()

    def __repr__(self) -> str:
        return f"<RequestItem url={self.url}, data={self.data}>"
