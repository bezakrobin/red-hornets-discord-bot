import discord
import json


# LOAD JSON DATA
def load_data(file_name='data.json'):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


# SAVE JSON DATA
def save_data(data, file_name='data.json'):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


# SEND WELCOME MESSAGE
async def send_welcome_message(member, client, welcome_channel_id):
    welcome_channel = client.get_channel(int(welcome_channel_id))
    if welcome_channel:
        embed = discord.Embed(
            title=f"Welcome @{member.name}!",
            description=f"Thanks for joining {member.guild.name}! We're glad to have you here.",
            color=discord.Color.red()
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        await welcome_channel.send(embed=embed)


# CREATE SERVER STATS
async def create_server_stats(client, guild_id):
    data = load_data()
    guild = client.get_guild(int(guild_id))
    category = await create_category(guild, '📊 SERVER STATS 📊', 0)
    await create_locked_channel(guild, f"MEMBERS: {data['member_count']}", 'voice', category)


# CREATE CATEGORY
async def create_category(guild, category_name: str, position: int):
    new_category = await guild.create_category(name=category_name, position=position)
    return new_category


# CREATE CHANNEL
async def create_channel(guild, channel_name: str, channel_type: str, category: discord.CategoryChannel = None):
    if channel_type == 'text':
        new_channel = await guild.create_text_channel(name=channel_name, category=category)
    elif channel_type == 'voice':
        new_channel = await guild.create_voice_channel(name=channel_name, category=category)
    else:
        raise ValueError("Channel type must be 'text' or 'voice'")
    return new_channel


# CREATE LOCKED CHANNEL
async def create_locked_channel(guild, channel_name: str, channel_type: str,  category: discord.CategoryChannel = None):
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
