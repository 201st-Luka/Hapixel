from abc import ABC, abstractmethod
from sys import stderr

from aiohttp import ClientResponse

from ..collections.exceptions import RequestNotDone
from ..core import Client
from ..utils.request_item import RequestItem
from ..utils import Missing, MISSING


__all__ = (
    'BaseAuthRequest',
    'BaseRequest',
)


class BaseAuthRequest(ABC):
    @abstractmethod
    def __init__(self, endpoint_url: str, **request_params):
        self.__url = endpoint_url
        self.__request_params = {k: v for k, v in request_params.items() if v is not None}

        self._response: ClientResponse | None = None
        self._json: dict | None = None
        self._exception: Exception | None = None

    async def request(self, client_id: int | str = None) -> 'BaseAuthRequest':
        client = Client.instance_from_id(client_id)

        request_item = RequestItem(self.__url, self.__request_params)

        await client.queue.put(request_item)

        future = await request_item.future

        self._response, self._json, self._exception = future

        if self._exception is not None:
            if client.raise_exceptions:
                raise self._exception
            elif client.logging:
                client.logger.error(f"Exception occurred while requesting {self.__class__.__name__}: "
                                    f"{self._exception}",)
            else:
                print(f"Exception occurred while requesting {self.__class__.__name__}: "
                      f"{self._exception}", file=stderr)

        return self

    def _get_data(self, key: str) -> int | str | dict | list | None | Missing:
        if self._json is None:
            raise RequestNotDone()
        if key not in self._json:
            return MISSING
        return self._json[key]

    def __repr__(self) -> str:
        return (f"<{self.__class__.__name__} endpoint_url={self.__url}, "
                f"request_data={self.__request_params}>")

    @property
    def endpoint_url(self) -> str:
        return self.__url

    @property
    def request_data(self) -> dict | str | int | None:
        return self.__request_params

    @property
    def response(self) -> ClientResponse | None:
        return self._response

    @property
    def json(self) -> dict | None:
        return self._json

    @property
    def success(self):
        return self._get_data('success')


class BaseRequest(BaseAuthRequest, ABC):

    async def request(self, client_id: int | str = None) -> 'BaseAuthRequest':
        client = Client.instance_from_id(client_id)

        self._response, self._json = await client.consumer.get(self.endpoint_url, **self.request_data)

        return self
