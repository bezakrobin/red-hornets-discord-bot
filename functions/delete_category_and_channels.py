import discord


async def delete_category_and_channels(category: discord.CategoryChannel):
    """Deletes a category and all channels within it.

    Args:
    category (discord.CategoryChannel): The category to delete along with its channels.
    """
    # Delete all channels in the category
    for channel in category.channels:
        await channel.delete(reason="Deleting channel within category.")

    # Now delete the category itself
    await category.delete(reason="Deleting category.")
