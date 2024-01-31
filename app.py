import discord
from discord import app_commands
import os
from flask import Flask
from threading import Thread
from functions.send_welcome_message import send_welcome_message
from functions.create_category import create_category
from functions.create_locked_channel import create_locked_channel
from functions.load_data import load_data
from functions.save_data import save_data
from functions.delete_category_and_channels import delete_category_and_channels


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
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# COMMANDS
@tree.command(
    name="serverstats",
    description="This command will create a server status category with status data.",
    guild=discord.Object(id=int(GUILD_ID))
)
async def serverstats(interaction):
    data = load_data()
    if data['service_stats_category'] is not None:
        category_to_delete = interaction.client.get_channel(int(data['service_stats_category']))
        await delete_category_and_channels(category_to_delete)
    guild = interaction.client.get_guild(int(GUILD_ID))
    category = await create_category(guild, '📊 SERVER STATS 📊', 0)
    data['server_stats_category'] = category.id
    save_data(data)
    await create_locked_channel(guild, f"MEMBERS: {data['member_count']}", 'voice', category)
    await create_locked_channel(guild, f"SUGGESTIONS: {data['suggestions_count']}", 'voice', category)
    await create_locked_channel(guild, f"SUGGESTIONS DONE: {data['suggestions_done_count']}", 'voice', category)
    await create_locked_channel(guild, f"BUGS: {data['bugs_count']}", 'voice', category)
    await create_locked_channel(guild, f"BUGS FIXED: {data['bugs_fixed_count']}", 'voice', category)


# ON READY EVENT
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=int(GUILD_ID)))


# ON MEMBER JOIN EVENT
@client.event
async def on_member_join(member):
    await send_welcome_message(member, client, WELCOME_CHANNEL_ID)


# FLASK & BOT START
keep_alive()
client.run(BOT_TOKEN)
