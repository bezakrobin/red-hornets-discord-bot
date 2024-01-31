import discord
from discord import app_commands
import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "I'm alive!"


# ENV VARIABLES
BOT_TOKEN = os.environ.get('BOT_TOKEN')
GUILD_ID = os.environ.get('GUILD_ID')
WELCOME_CHANNEL_ID = os.environ.get('WELCOME_CHANNEL_ID')

# BOT SETUP
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# ON MEMBER JOIN EVENT
@client.event
async def on_member_join(member):
    welcome_channel = client.get_channel(int(WELCOME_CHANNEL_ID))
    if welcome_channel:
        embed = discord.Embed(
            title=f"Welcome {member.name}!",
            description=f"Thanks for joining {member.guild.name}! We're glad to have you here.",
            color=discord.Color.green()
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        await welcome_channel.send(embed=embed)


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


client.run(BOT_TOKEN)
