import discord
import json


async def server_stats(client, guild_id, bug_report_channel_id):
    with open('data.json', 'r') as file:
        data = json.load(file)

    guild = client.get_guild(int(guild_id))

    category_id = data.get('server_stats_category_id')
    if category_id:
        category = discord.utils.get(guild.categories, id=int(category_id))
        if category:
            for channel in category.channels:
                await channel.delete()
            await category.delete()

    new_category = await guild.create_category('📊 SERVER STATS 📊')

    await new_category.edit(position=0)

    data['server_stats_category_id'] = new_category.id
    with open('data.json', 'w') as file:
        json.dump(data, file)

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(connect=False)
    }

    channel = client.get_channel(bug_report_channel_id)

    bugs_reported_message_count = 0

    async for _ in channel.history(limit=None):
        bugs_reported_message_count += 1

    # TODO BUGS FIXED
    await guild.create_voice_channel(f"MEMBERS: {guild.member_count}", category=new_category, overwrites=overwrites)
    # await guild.create_voice_channel(f"BUGS FIXED: 0", category=new_category, overwrites=overwrites)
    await guild.create_voice_channel(f"BUGS REPORTED: {bugs_reported_message_count}", category=new_category, overwrites=overwrites)

    print(f'Updated server stats for {guild.name} server')
