import discord


async def create_voice_channel(guild: discord.Guild, channel_name: str, category_id: int, position: int) -> int:
    """
    Create a voice channel under a specified category and set its position.

    Parameters:
    - guild: The discord.Guild object where the channel will be created.
    - channel_name: The name of the voice channel to be created.
    - category_id: The ID of the category under which the channel will be created.
    - position: The position of the channel within the category.

    Returns:
    - The ID of the created voice channel.
    """
    category = guild.get_channel(category_id)
    if category is None or not isinstance(category, discord.CategoryChannel):
        raise ValueError("Invalid category ID or category does not exist")

    voice_channel = await guild.create_voice_channel(channel_name, category=category)

    await voice_channel.edit(position=position)

    return voice_channel.id
