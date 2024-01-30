import discord
from discord import app_commands
import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')
GUILD_ID = os.environ.get('GUILD_ID')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(
    name="commandname",
    description="My first application Command",
    guild=discord.Object(id=int(GUILD_ID))
)
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=int(GUILD_ID)))
    print("Ready!")

client.run(BOT_TOKEN)