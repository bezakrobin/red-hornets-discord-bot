async def count_members(client, guild_id):
    guild = client.get_guild(int(guild_id))
    return len(guild.members)
