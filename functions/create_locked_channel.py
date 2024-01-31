import discord


async def create_locked_channel(guild, channel_name: str, channel_type: str, category: discord.CategoryChannel = None):
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(send_messages=False, connect=False)
    }
    if channel_type == 'text':
        new_channel = await guild.create_text_channel(name=channel_name, overwrites=overwrites, category=category)
    elif channel_type == 'voice':
        new_channel = await guild.create_voice_channel(name=channel_name, overwrites=overwrites, category=category)
    else:
        raise ValueError("Channel type must be 'text' or 'voice'")
    return new_channel
