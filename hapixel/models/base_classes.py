from enum import Enum
from typing import TypeVar, Generic, Iterator, Callable, List

from ..collections import RequestNotDone
from ..utils import MISSING, Missing, snake_to_camel_case

__all__ = (
    'BaseResponse',
    'BaseIterator',
    'FieldFormatter',
    'BaseEnumGetter',
    'Factory',
)

T = TypeVar('T')
U = TypeVar('U')


class FieldFormatter:
    def __init__(self, key_name: str = None, type_: type = None, sub_type: type = None):
        self.key_name = key_name
        self.type = type_
        self.sub_type = sub_type


class ResponseMeta(type):
    def __new__(mcs, name, bases, namespace: dict, **kwargs):
        __annotations = namespace.get('__annotations__')

        if __annotations is None:
            return super(ResponseMeta, mcs).__new__(mcs, name, bases, namespace, **kwargs)

        __annots = {
            arg: FieldFormatter(
                snake_to_camel_case(arg), annot
            ) if arg not in namespace else FieldFormatter(
                namespace[arg].key_name or snake_to_camel_case(arg),
                namespace[arg].type or annot,
                namespace[arg].sub_type
            )
            for arg, annot in __annotations.items()
            if arg not in namespace or isinstance(namespace[arg], FieldFormatter)
        }

        namespace.update({
            arg: property(
                (lambda self, f=field:
                 f.type(self._get_json(f.key_name))) if field.sub_type is None else
                (lambda self, f=field:
                 f.type(self._get_json(f.key_name), f.sub_type))
            )
            for arg, field in __annots.items()
        })

        return super(ResponseMeta, mcs).__new__(mcs, name, bases, namespace, **kwargs)


class BaseResponse(metaclass=ResponseMeta):
    def __new__(cls, json: dict | Missing | None = None, *args, **kwargs):
        if json is MISSING:
            return MISSING
        return super().__new__(cls)

    def __init__(self, json: dict | Missing | None = None):
        self._exception: Exception | None = None
        self._json = json

    def _get_json(self, key: str) -> int | str | dict | list | None | Missing:
        if hasattr(self, '_exception') and self._exception:
            raise self._exception
        if self._json is None:
            raise RequestNotDone()
        if key not in self._json:
            return MISSING
        return self._json[key]

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} json={'{' + ', '.join(f'{key}' for key in self._json.keys()) + '}'}>"

    @property
    def json(self) -> dict | None:
        return self._json

    @json.setter
    def json(self, new_json: dict):
        self._json = new_json


class Factory:
    def __init__(
            self,
            base: Callable[[dict], T] | Callable[[list], T] | Callable[[dict, ...], T] | Callable[[list, ...], T],
            *args: Callable[[dict], T] | Callable[[list], T] | Callable[[dict, ...], T] | Callable[[list, ...], T]
    ):
        self.__base = base
        self.__args = args

    def __call__(self, json: dict | list) -> T:
        return self.__base(json, *self.__args)

    @property
    def factory_args(self) -> tuple[
        Callable[[dict], T] | Callable[[dict, T, ...], T] | Callable[[list, T, ...], T], ...
    ]:
        return self.__args

    @property
    def factory_base(self) -> Callable[[dict], T] | Callable[[dict, T, ...], T] | Callable[[list, T, ...], T]:
        return self.__base

    def __repr__(self) -> str:
        return (
            f"<Factory of type '{self.__base.__name__}' with args {', '.join(f'{arg}' for arg in self.__args)}>"
            if self.__args else
            f"<Factory of type '{self.__base.__name__}'>"
        )


class BaseEnumGetter(BaseResponse, Generic[T]):
    _factory: Factory

    def get_value(self, enum: Enum) -> T:
        """
        Get the value of the enum from the json.

        Args:
            enum (Enum):
                The enum to get the value of.

        Returns:
            T:
                The value of the enum (type cast).
        """
        return self._factory(self._get_json(enum.name))

    def __len__(self) -> int:
        return len(self._json)

    def __getattr__(self, item: str) -> T:
        return self._factory(self._get_json(item))

    def __getitem__(self, item: str | Enum) -> T:
        if isinstance(item, Enum):
            item = item.name
        return self._factory(self._get_json(item))

    def __iter__(self) -> Iterator[T]:
        return (self._factory(item) for item in self._json.values())

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} of type '{self._factory.factory_base.__name__}'>"


class BaseIterator[T]:
    def __init__(self, data: List[U] | List[T], raw: bool = True):
        if raw:
            self.__raw_data = data
            self.__data = None
        else:
            self.__data = data
            self.__raw_data = None

    def __transform_data(self):
        self.__data = [self.__orig_class__.__args__[0](item) for item in self.__raw_data]

    def __iter__(self) -> Iterator[T]:
        if self.__data is None:
            self.__transform_data()
        return iter(self.__data)

    def __len__(self) -> int:
        return len(self.__raw_data)

    def __getitem__(self, item) -> T:
        if self.__data is None:
            self.__transform_data()
        return self.__data[item]

    def __call__(
            self,
            sort: bool = False,
            key: Callable = None,
            filter_: Callable[[T], bool] = None
    ) -> 'BaseIterator[T]':
        if self.__data is None:
            self.__transform_data()

        data = self.__data.copy()

        if sort:
            data.sort(key=key)

        if filter_ is not None:
            filter(filter_, data)

        return self.__class__[self.__orig_class__.__args__[0]](data.copy(), raw=False)

    def __repr__(self) -> str:
        return (f"<{self.__class__.__name__} of type '"
                f"{self.__orig_class__.__args__[0].__name__ if hasattr(self, '__orig_class__') else self.__raw_data[0].__class__.__name__}"
                f"', len={len(self)}>")
