import discord
import os
from flask import Flask
from threading import Thread
from utils.get_member_count import get_member_count
from utils.set_channel_name_by_id import set_channel_name_by_id


app = Flask(__name__)


@app.route('/')
def home():
    return "I'm alive!"


def run():
    app.run(host='0.0.0.0', port=10000)


def keep_alive():
    t = Thread(target=run)
    t.start()


bot_token = os.environ.get('BOT_TOKEN')
guild_id = os.environ.get('GUILD_ID')
channel_member_count = os.environ.get('MEMBER_COUNT_ID')
welcome_channel_id = os.environ.get('WELCOME_CHANNEL_ID')


intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}.')
    guild = client.get_guild(int(guild_id))
    await set_channel_name_by_id(guild, int(channel_member_count), f"MEMBERS: {await get_member_count(guild)}")


@client.event
async def on_member_join(member):
    print(f'{member.name} has joined the server.')
    welcome_channel = client.get_channel(int(welcome_channel_id))
    if welcome_channel:
        embed = discord.Embed(
            title=f"Welcome {member.name}!",
            description=f"Thanks for joining {member.guild.name}! We're glad to have you here.",
            color=discord.Color.red()
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        await welcome_channel.send(embed=embed)
    guild = client.get_guild(int(guild_id))
    await set_channel_name_by_id(guild, int(channel_member_count), f"MEMBERS: {await get_member_count(guild)}")


@client.event
async def on_member_remove(member):
    print(f'{member.name} has left the server.')
    guild = client.get_guild(int(guild_id))
    await set_channel_name_by_id(guild, int(channel_member_count), f"MEMBERS: {await get_member_count(guild)}")


keep_alive()
client.run(bot_token)
