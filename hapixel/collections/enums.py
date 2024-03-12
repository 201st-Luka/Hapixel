from enum import Enum


__all__ = (
    'HapixelStatus',
    'Games',
    'Servers'
)


class HapixelStatus(Enum):
    PAUSED    = 0
    RUNNING   = 1
    THROTTLED = 2


class Games(Enum):
    QUAKECRAFT     = 'QUAKECRAFT'
    WALLS          = 'WALLS'
    PAINTBALL      = 'PAINTBALL'
    SURVIVAL_GAMES = 'SURVIVAL_GAMES'
    TNTGAMES       = 'TNTGAMES'
    VAMPIREZ       = 'VAMPIREZ'
    WALLS3         = 'WALLS3'
    ARCADE         = 'ARCADE'
    ARENA          = 'ARENA'
    UHC            = 'UHC'
    MCGO           = 'MCGO'
    BATTLEGROUND   = 'BATTLEGROUND'
    SUPER_SMASH    = 'SUPER_SMASH'
    GINGERBREAD    = 'GINGERBREAD'
    HOUSING        = 'HOUSING'
    SKYWARS        = 'SKYWARS'
    TRUE_COMBAT    = 'TRUE_COMBAT'
    SPEED_UHC      = 'SPEED_UHC'
    SKYCLASH       = 'SKYCLASH'
    LEGACY         = 'LEGACY'
    PROTOTYPE      = 'PROTOTYPE'
    BEDWARS        = 'BEDWARS'
    MURDER_MYSTERY = 'MURDER_MYSTERY'
    BUILD_BATTLE   = 'BUILD_BATTLE'
    DUELS          = 'DUELS'
    SKYBLOCK       = 'SKYBLOCK'
    PIT            = 'PIT'
    REPLAY         = 'REPLAY'
    SMP            = 'SMP'
    WOOL_GAMES     = 'WOOL_GAMES'

    @classmethod
    def from_id(cls, id_: int) -> 'Games':
        id_matcher = {
            2:  'QUAKECRAFT',
            3:  'WALLS',
            4:  'PAINTBALL',
            5:  'SURVIVAL_GAMES',
            6:  'TNTGAMES',
            7:  'VAMPIREZ',
            13: 'WALLS3',
            14: 'ARCADE',
            17: 'ARENA',
            20: 'UHC',
            21: 'MCGO',
            23: 'BATTLEGROUND',
            24: 'SUPER_SMASH',
            25: 'GINGERBREAD',
            26: 'HOUSING',
            51: 'SKYWARS',
            52: 'TRUE_COMBAT',
            54: 'SPEED_UHC',
            55: 'SKYCLASH',
            56: 'LEGACY',
            57: 'PROTOTYPE',
            58: 'BEDWARS',
            59: 'MURDER_MYSTERY',
            60: 'BUILD_BATTLE',
            61: 'DUELS',
            63: 'SKYBLOCK',
            64: 'PIT',
            65: 'REPLAY',
            67: 'SMP',
            68: 'WOOL_GAMES'
        }

        return cls(id_matcher[id_])


class Servers(Enum):
    IDLE             = 'IDLE'
    LIMBO            = 'LIMBO'
    MAIN_LOBBY       = 'MAIN_LOBBY'
    QUEUE            = 'QUEUE'
    TOURNAMENT_LOBBY = 'TOURNAMENT_LOBBY'

