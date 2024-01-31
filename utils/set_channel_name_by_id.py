import discord


async def set_channel_name_by_id(guild: discord.Guild, channel_id: int, new_name: str):
    """
    Change the name of a channel by its ID in the specified guild.

    Parameters:
    - guild: The discord.Guild object where the channel exists.
    - channel_id: The ID of the channel to rename.
    - new_name: The new name to set for the channel.
    """
    channel = guild.get_channel(channel_id)
    if channel:
        await channel.edit(name=new_name)
    else:
        print(f"No channel found with ID {channel_id}.")
