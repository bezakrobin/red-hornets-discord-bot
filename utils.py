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


# COUNT MEMBERS
async def count_members(client, guild_id):
    guild = client.get_guild(int(guild_id))
    return len(guild.members)
