async def get_channel_containing(client, guild_id, search_string):
    guild = client.get_guild(int(guild_id))
    for channel in guild.channels:
        if search_string.upper() in channel.name.upper():
            return channel
    return None
