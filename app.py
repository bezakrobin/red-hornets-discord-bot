import discord
from discord import app_commands
import os
from flask import Flask
from threading import Thread
import json


# FLASK WEB SERVER
app = Flask(__name__)


@app.route('/')
def home():
    return "I'm alive!"


def run():
    app.run(host='0.0.0.0', port=10000)


def keep_alive():
    t = Thread(target=run)
    t.start()


# ENV VARIABLES
BOT_TOKEN = os.environ.get('BOT_TOKEN')
GUILD_ID = os.environ.get('GUILD_ID')
WELCOME_CHANNEL_ID = os.environ.get('WELCOME_CHANNEL_ID')
SERVER_STATS_CATEGORY_ID = os.environ.get('SERVER_STATS_CATEGORY_ID')


# BOT SETUP
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# ON MEMBER JOIN EVENT
@client.event
async def on_member_join(member):
    send_welcome_message(member)


# SLASH COMMANDS
@tree.command(
    name="commandname",
    description="My first application Command",
    guild=discord.Object(id=int(GUILD_ID))
)
async def first_command(interaction):
    await interaction.response.send_message("Hello!")


# ON READY EVENT
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=int(GUILD_ID)))
    print("Ready!")


# FLASK & BOT START
keep_alive()
client.run(BOT_TOKEN)


# FUNCTIONS
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
async def send_welcome_message(member):
    welcome_channel = client.get_channel(int(WELCOME_CHANNEL_ID))
    if welcome_channel:
        embed = discord.Embed(
            title=f"Welcome @{member.name}!",
            description=f"Thanks for joining {member.guild.name}! We're glad to have you here.",
            color=discord.Color.red()
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        await welcome_channel.send(embed=embed)
