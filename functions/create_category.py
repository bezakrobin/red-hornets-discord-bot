async def create_category(guild, category_name, position=None):
    """Create a new category in the specified guild with the given position.

    Args:
    guild (discord.Guild): The guild to create the category in.
    category_name (str): The name of the category to create.
    position (int, optional): The position in the guild's channel list. Defaults to None.

    Returns:
    discord.CategoryChannel: The created category.
    """
    new_category = await guild.create_category(name=category_name, position=position)
    return new_category
