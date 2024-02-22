from aiohttp import ClientSession


__all__ = (
    'uuid_from_username',
    'snake_to_camel_case'
)


async def uuid_from_username(username: str) -> str:
    async with ClientSession() as session:
        async with session.get(f"https://api.mojang.com/users/profiles/minecraft/{username}") as response:
            data = await response.json()
            return data["id"]


def snake_to_camel_case(string: str) -> str:
    words = string.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

