async def get_channel_by_name(client, guild_id, channel_name):
    guild = client.get_guild(int(guild_id))
    for channel in guild.channels:
        if channel.name == channel_name:
            return channel
    return None
