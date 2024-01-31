import discord


async def get_member_count(guild: discord.Guild) -> int:
    """
    Retrieve the member count of a guild (server).

    Parameters:
    - guild: The discord.Guild object for the guild.

    Returns:
    - The member count of the guild as an integer.
    """
    return guild.member_count
