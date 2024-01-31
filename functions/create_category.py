async def create_category(guild, category_name, position=None):
    new_category = await guild.create_category(name=category_name, position=position)
    return new_category
