from asyncio import create_task, sleep, Task, run
from time import perf_counter
from datetime import datetime

from aiohttp import ClientSession, ClientTimeout, ClientResponse

from ..collections import HapixelStatus, HapixelException
from ..utils import RequestItem

__all__ = (
    'Consumer',
)


class Timer:
    def __init__(self, client):
        self.__client = client
        self.__interval = client.request_wait_time

    async def __aenter__(self):
        self.__start = perf_counter()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.__end = perf_counter()
        elapsed = self.__end - self.__start

        if elapsed < self.__interval:
            await sleep(self.__interval - elapsed)

        if self.__client.rate_limit_remaining == 0:
            await sleep(self.__client.rate_limit_reset)


class Consumer:
    def __init__(
            self,
            client,
    ):
        self.__client = client

        self.__task: Task | None = None
        self.__header_session: ClientSession | None = None
        self.__session: ClientSession | None = None

        self.__status = HapixelStatus.PAUSED
        self.__client.logger.debug(f"Initialized {self.__class__.__name__} for client='{self.__client.id}'")

    def __repr__(self):
        return f"<{self.__class__.__name__} of client='{self.__client.id}'>"

    def __del__(self):
        if self.is_running():
            run(self.stop())

    async def __request(self, item: RequestItem):
        self.__client.logger.debug(f"Requesting item='{item}' for client='{self.__client.id}'")

        async with self.__header_session.get(
                f"{self.__client.version}/{item.url}",
                params=item.params,
        ) as response:
            self.__client.logger.debug(f"Got response={response} for item='{item}' for client='{self.__client.id}'")

            self.__client.last_request_time = datetime.strptime(
                response.headers['Date'],
                '%a, %d %b %Y %H:%M:%S %Z'
            )
            self.__client.rate_limit_limit = response.headers['RateLimit-Limit']
            self.__client.rate_limit_remaining = response.headers['RateLimit-Remaining']
            self.__client.rate_limit_reset = response.headers['RateLimit-Reset']

            item.future.set_result((response, await response.json()))

        self.__client.logger.info(f"Request for client='{self.__client.id}' with item='{item}' is done")

    async def __run(self):
        while True:
            async with Timer(self.__client):
                item = await self.__client.queue.get()

                self.__client.logger.debug(f"{self.__class__.__name__} for client='{self.__client.id}' got a request "
                                           f"item='{item}'")

                await self.__request(item)

                self.__client.queue.task_done()

    async def start(self):
        if self.is_running():
            raise HapixelException("Consumer is already running")
        else:
            self.__client.logger.debug(f"Starting {self.__class__.__name__} for client='{self.__client.id}'")
            self.__status = HapixelStatus.RUNNING

            self.__header_session = ClientSession(
                self.__client.base_url,
                timeout=ClientTimeout(total=self.__client.timeout),
                headers={
                    'API-Key': self.__client.api_key
                }
            )
            self.__session = ClientSession(
                self.__client.base_url,
                timeout=ClientTimeout(total=self.__client.timeout),
            )

            self.__task = create_task(self.__run())

            self.__client.logger.debug(f"Started {self.__class__.__name__} for client='{self.__client.id}'")

    async def stop(self):
        if not self.is_running():
            raise HapixelException("Consumer is not running, start the associated client first")
        else:
            self.__client.logger.debug(f"Stopping {self.__class__.__name__} for client='{self.__client.id}'")
            self.__status = HapixelStatus.PAUSED

            await self.__header_session.close()
            self.__header_session = None
            await self.__session.close()
            self.__session = None
            self.__task.cancel()
            self.__task = None

            self.__client.logger.debug(f"Stopped {self.__class__.__name__} for client='{self.__client.id}'")

    def is_running(self) -> bool:
        return self.__status == HapixelStatus.RUNNING

    async def get(self, endpoint_url: str, **request_params) -> tuple[ClientResponse, dict]:
        if not self.is_running():
            raise HapixelException("Consumer is not running, start the associated client first")

        self.__client.logger.debug(f"Requesting endpoint_url='{endpoint_url}' with request_params='{request_params}'")

        async with self.__session.get(
            f"{self.__client.version}/{endpoint_url}",
            params=request_params,
        ) as response:
            return response, await response.json()

    @property
    def task(self) -> Task | None:
        return self.__task

    @property
    def header_session(self) -> ClientSession | None:
        return self.__header_session

    @property
    def session(self) -> ClientSession | None:
        return self.__session

    @property
    def status(self) -> HapixelStatus:
        return self.__status
