from enum import Enum


__all__ = (
    'HapixelStatus',
    'RequestType',
)


class HapixelStatus(Enum):
    PAUSED    = 0
    RUNNING   = 1
    THROTTLED = 2


class RequestType(Enum):
    WITH_AUTH = 0
    NO_AUTH   = 1
