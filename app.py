import discord
import os
from flask import Flask
from threading import Thread
from utils.init.init_data import init_data
from utils.init.init_categories import init_categories


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
bot_token = os.environ.get('BOT_TOKEN')
guild_id = os.environ.get('GUILD_ID')


# BOT SETUP
intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = discord.Client(intents=intents)


# ON READY EVENT
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}.')
    guild = client.get_guild(int(guild_id))
    await init_data()
    await init_categories(guild)


# FLASK & BOT START
keep_alive()
client.run(bot_token)
