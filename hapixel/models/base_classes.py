from typing import TypeVar, Generic, Iterator, Callable, List

from ..collections import RequestNotDone
from ..utils import MISSING, Missing, snake_to_camel_case

__all__ = (
    'BaseResponse',
    'BaseIterator',
    'FieldFormatter',
)

T = TypeVar('T')
U = TypeVar('U')


class FieldFormatter:
    def __init__(self, key_name: str = None, type_: type = None, sub_type: type = None):
        self.key_name = key_name
        self.type = type_
        self.sub_type = sub_type


class ResponseMeta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        annotations = namespace.get('__annotations__')

        if annotations is None:
            return super(ResponseMeta, mcs).__new__(mcs, name, bases, namespace, **kwargs)

        annots = {
            arg: FieldFormatter(
                snake_to_camel_case(arg), annot
            ) if arg not in namespace else FieldFormatter(
                namespace[arg].key_name or snake_to_camel_case(arg),
                namespace[arg].type or annot,
                namespace[arg].sub_type
            )
            for arg, annot in annotations.items()
            if arg not in namespace or isinstance(namespace[arg], FieldFormatter)
        }

        for arg, field in annots.items():
            namespace[arg] = property(
                (lambda self, f=field:
                    f.type(self._get_json(f.key_name))) if field.sub_type is None else
                (lambda self, f=field:
                    f.type(self._get_json(f.key_name), f.sub_type))
            )
            del namespace['__annotations__'][arg]

        if namespace['__annotations__'] == {}:
            del namespace['__annotations__']

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
        if hasattr(self, '_exception') and self._exception is not None:
            raise self._exception
        if self._json is None:
            raise RequestNotDone()
        if key not in self._json:
            return MISSING
        return self._json[key]

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} json={self._json}>"

    @property
    def json(self) -> dict | None:
        return self._json

    @json.setter
    def json(self, new_json: dict):
        self._json = new_json

    success: bool


class BaseIterator(Generic[T]):
    def __init__(self, data: List[U], factory: Callable[[U], T]):
        self.__data = data
        self.__factory = factory

    def __iter__(self) -> Iterator[T]:
        return (self.__factory(item) for item in self.__data)

    def __len__(self) -> int:
        return len(self.__data)

    def __getitem__(self, item) -> T:
        return self.__factory(self.__data[item])

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} of type '{type(self.__factory)}', len={len(self)}>"
