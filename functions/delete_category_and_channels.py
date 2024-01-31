import discord


async def delete_category_and_channels(category: discord.CategoryChannel):
    """Deletes a category and all channels within it.

    Args:
    category (discord.CategoryChannel): The category to delete along with its channels.
    """
    for channel in category.channels:
        await channel.delete(reason="Deleting channel within category.")
    await category.delete(reason="Deleting category.")
