async def get_category_by_name(client, guild_id, category_name):
    guild = client.get_guild(int(guild_id))
    for category in guild.categories:
        if category.name == category_name:
            return category
    return None
