from asyncio import run, Queue
from logging import getLogger, Logger

from .consumer import Consumer
from ..collections import HapixelException, HapixelStatus, ApiKeyException
from ..utils import MISSING, Missing

__all__ = (
    'Client',
)


class Client:
    base_url = "https://api.hypixel.net"
    version = "/v2"
    requests_per_second = 10
    requests_per_second_auth = 10

    __instances: list['Client'] = []

    def __new__(
            cls,
            *,
            custom_id: str = None,
            **kwargs
    ) -> 'Client':
        if custom_id is not None:
            if not isinstance(custom_id, str):
                raise HapixelException("Custom ID must be a string")
            if custom_id == "":
                raise HapixelException("Custom ID cannot be an empty string")
            if custom_id.isspace():
                raise HapixelException("Custom ID cannot be a whitespace string")
            if custom_id.isdigit():
                raise HapixelException("Custom ID cannot be a string of a number")
            if custom_id in [instance.__id for instance in Client.__instances]:
                raise HapixelException("Client with this ID already exists")
        return super().__new__(cls)

    def __init__(
            self,
            api_key: str,
            *,
            default_logging: bool = False,
            custom_id: str = None,
            logger: Logger = MISSING,
            request_timeout: float = 30,
    ):
        if default_logging:
            if logger is not MISSING:
                raise HapixelException("Cannot enable default logging and provide a custom logger")
            self.__logger = getLogger("hapixel")
        else:
            if logger is not MISSING and not isinstance(logger, Logger):
                raise HapixelException("Logger must be an instance of logging.Logger")
            self.__logger = logger

        self.__logger.debug(f"Creating new instance of {self.__class__.__name__}")

        self.__logger.debug(
            f"Initializing {self.__class__.__name__} with the following parameters:\n"
            f"\tapi_key={api_key}, default_logging={default_logging}, custom_id={custom_id}, "
            f"logger={logger}, request_timeout={request_timeout}"
        )

        if not isinstance(api_key, str):
            raise ApiKeyException("API key must be a string")
        if api_key == "":
            raise ApiKeyException("API key cannot be an empty string")
        self.__api_key = api_key
        self.__status = HapixelStatus.PAUSED
        if custom_id is not None:
            self.__id = custom_id
        else:
            self.__id = len(Client.__instances)

        self.timeout = request_timeout

        self.__logger.debug(f"Initializing queue for {self.__class__.__name__} with id={self.__id}")
        self.__queue = Queue()

        self.__logger.debug(f"Initializing consumer for {self.__class__.__name__} with id={self.__id}")
        self.__consumer = Consumer(self)

        Client.__instances.append(self)

        self.__logger.info(f"Initialized {self.__class__.__name__} with id={self.__id}")

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id={self.__id}>"

    def __del__(self):
        self.__logger.debug(f"Deleting {self.__class__.__name__} with id={self.__id}")

        if self.is_running():
            run(self.stop_client())

        Client.__instances.remove(self)

        self.__logger.debug(f"Deleted {self.__class__.__name__} with id={self.__id}")

    async def __aenter__(self) -> 'Client':
        await self.start_client()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.stop_client()

    def enable_logging(self):
        if self.__logger is MISSING:
            self.__logger = getLogger("hapixel")
        else:
            raise HapixelException("Logging is already enabled")

    def disable_logging(self):
        if self.__logger is not MISSING:
            self.__logger = MISSING
        else:
            raise HapixelException("Logging is already disabled")

    async def start_client(self):
        if self.is_running():
            raise HapixelException("Client is already running")
        else:
            self.__logger.debug(f"Starting {self.__class__.__name__} with id={self.__id}")
            self.__status = HapixelStatus.RUNNING

            await self.__consumer.start()
            self.__logger.info(f"Started {self.__class__.__name__} with id={self.__id}")

    async def stop_client(self):
        if not self.is_running():
            raise HapixelException("Client is not running")
        else:
            self.__logger.debug(f"Stopping {self.__class__.__name__} with id={self.__id}")
            self.__status = HapixelStatus.PAUSED

            await self.__consumer.stop()
            self.__logger.info(f"Stopped {self.__class__.__name__} with id={self.__id}")

    @property
    def id(self) -> int | str:
        return self.__id

    @id.setter
    def id(self, new_id: str):
        if new_id in [instance.__id for instance in Client.__instances]:
            raise HapixelException("Client with this ID already exists")
        self.__id = new_id

    @property
    def queue(self) -> Queue:
        return self.__queue

    @property
    def consumer(self) -> Consumer:
        return self.__consumer

    @property
    def api_key(self) -> str | None:
        return self.__api_key

    @property
    def logger(self) -> Logger | Missing:
        return self.__logger

    def is_running(self) -> bool:
        return self.__status == HapixelStatus.RUNNING

    @classmethod
    def instance_from_id(cls, id_: int | str | None) -> 'Client':
        if not len(cls.__instances):
            raise HapixelException("No clients exist")

        if id_ is None:
            return cls.__instances[0]

        for instance in cls.__instances:
            if instance.id == id_:
                return instance

        raise HapixelException("No client with this ID exists")

    @classmethod
    def instances(cls) -> list['Client']:
        return cls.__instances
