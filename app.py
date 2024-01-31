import discord
from discord import app_commands
import os
from flask import Flask
from threading import Thread
from utils import create_server_stats, send_welcome_message


# FLASK WEB SERVER
app = Flask(__name__)


@app.route('/')
def home():
    return "I'm alive!"


def run():
    app.run(host='0.0.0.0', port=10000)


# ENV VARIABLES
BOT_TOKEN = os.environ.get('BOT_TOKEN')
GUILD_ID = os.environ.get('GUILD_ID')
WELCOME_CHANNEL_ID = os.environ.get('WELCOME_CHANNEL_ID')


# BOT SETUP
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# ON READY EVENT
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=int(GUILD_ID)))


# ON MEMBER JOIN EVENT
@client.event
async def on_member_join(member):
    await send_welcome_message(member, client, WELCOME_CHANNEL_ID)


# FLASK & BOT START
run()
client.run(BOT_TOKEN)
