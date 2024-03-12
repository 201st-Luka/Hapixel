from .rank import Rank
from .member import Member
from .base_classes import BaseResponse, FieldFormatter, BaseIterator
from ..collections import Games


class Guild(BaseResponse):
    id: str = FieldFormatter("_id", str)
    name: str
    name_lower: str
    coins: int
    coins_ever: int
    created: int
    members: BaseIterator[Member]
    ranks: BaseIterator[Rank]
    achievements: dict
    exp: int
    publicly_listed: bool
    preferred_games: BaseIterator[Games]
    description: str
    tag: str
    tag_color: str
    chat_mute: int
    guild_exp_by_game_type: dict
