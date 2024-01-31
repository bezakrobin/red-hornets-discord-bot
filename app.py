import discord
import os
from flask import Flask
from threading import Thread
from functions.welcome_message import welcome_message
from functions.server_stats import server_stats


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


# BOT SETUP
intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = discord.Client(intents=intents)


# ON READY EVENT
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}.')
    await server_stats(client, GUILD_ID)


# ON MEMBER JOIN EVENT
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')
    await welcome_message(client, member, WELCOME_CHANNEL_ID)
    await server_stats(client, GUILD_ID)


# ON MEMBER REMOVE EVENT
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')
    await server_stats(client, GUILD_ID)

# FLASK & BOT START
keep_alive()
client.run(BOT_TOKEN)
