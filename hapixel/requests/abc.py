from abc import ABC

from aiohttp import ClientResponse

from hapixel.utils.request_item import RequestItem
from ..core import Client


class BaseRequest(ABC):
    def __init__(self, endpoint_url: str, **request_data):
        self.__url = endpoint_url
        self.__request_data = {k: v for k, v in request_data.items() if v is not None}

        self.__response = None
        self.__json = None

    async def request(self, client_id: int | str = None):
        client = Client.instance_from_id(client_id)

        request_item = RequestItem(self.__url, self.__request_data)

        await client.queue.put(request_item)

        future = await request_item.future

        self.__response, self.__json = future

    def __repr__(self) -> str:
        return (f"<{self.__class__.__name__} endpoint_url={self.__url}, "
                f"request_data={self.__request_data}>")

    @property
    def endpoint_url(self) -> str:
        return self.__url

    @property
    def request_data(self) -> dict | str | int | None:
        return self.__request_data

    @property
    def response(self) -> ClientResponse | None:
        return self.__response

    @property
    def json(self) -> dict | None:
        return self.__json
