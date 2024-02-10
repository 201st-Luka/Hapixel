from aiohttp import ClientSession


async def uuid_from_username(username: str) -> str:
    async with ClientSession() as session:
        async with session.get(f"https://api.mojang.com/users/profiles/minecraft/{username}") as response:
            data = await response.json()
            return data["id"]
