import discord
from utils.structures.structures import structures
from utils.functions.create_category import create_category
from utils.functions.create_voice_channel import create_voice_channel
from utils.functions.create_text_channel import create_text_channel


async def init_categories(guild: discord.Guild):
    categories = await structures()

    for index, category in enumerate(categories):
        if category.__class__.__name__ == "Category":
            category_id = await create_category(guild, category.name, index)
        for channel_index, channel in enumerate(category.channels):
            if channel.__class__.__name__ == "VoiceChannel":
                channel_id = await create_voice_channel(guild, channel.name, category_id, channel_index)
            if channel.__class__.__name__ == "TextChannel":
                channel_id = await create_text_channel(guild, channel.name, category_id, channel_index)
