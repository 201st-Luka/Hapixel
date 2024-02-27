from enum import Enum


__all__ = (
    'HapixelStatus',
    'RequestType',
    'Games',
    'Servers'
)


class HapixelStatus(Enum):
    PAUSED    = 0
    RUNNING   = 1
    THROTTLED = 2


class RequestType(Enum):
    WITH_AUTH = 0
    NO_AUTH   = 1


class Games(Enum):
    QUAKECRAFT     = 2
    WALLS          = 3
    PAINTBALL      = 4
    SURVIVAL_GAMES = 5
    TNTGAMES       = 6
    VAMPIREZ       = 7
    WALLS3         = 13
    ARCADE         = 14
    ARENA          = 17
    UHC            = 20
    MCGO           = 21
    BATTLEGROUND   = 23
    SUPER_SMASH    = 24
    GINGERBREAD    = 25
    HOUSING        = 26
    SKYWARS        = 51
    TRUE_COMBAT    = 52
    SPEED_UHC      = 54
    SKYCLASH       = 55
    LEGACY         = 56
    PROTOTYPE      = 57
    BEDWARS        = 58
    MURDER_MYSTERY = 59
    BUILD_BATTLE   = 60
    DUELS          = 61
    SKYBLOCK       = 63
    PIT            = 64
    REPLAY         = 65
    SMP            = 67
    WOOL_GAMES     = 68


class Servers(Enum):
    IDLE             = 'IDLE'
    LIMBO            = 'LIMBO'
    MAIN_LOBBY       = 'MAIN_LOBBY'
    QUEUE            = 'QUEUE'
    TOURNAMENT_LOBBY = 'TOURNAMENT_LOBBY'

