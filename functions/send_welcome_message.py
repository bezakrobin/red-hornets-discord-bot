import discord


async def send_welcome_message(member, client, welcome_channel_id):
    welcome_channel = client.get_channel(int(welcome_channel_id))
    if welcome_channel:
        embed = discord.Embed(
            title=f"Welcome {member.name}!",
            description=f"Thanks for joining {member.guild.name}! We're glad to have you here.",
            color=discord.Color.red()
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        await welcome_channel.send(embed=embed)
