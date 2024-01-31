import discord


async def create_category(guild: discord.Guild, category_name: str, position: int) -> int:
    """
    Create a category in the specified guild, set its position, and return its ID.

    Parameters:
    - guild: The discord.Guild object where the category will be created.
    - category_name: The name of the category to be created.
    - position: The position to set for the category.

    Returns:
    - The ID of the created category.
    """
    category = await guild.create_category(category_name)
    await category.edit(position=position)
    return category.id
