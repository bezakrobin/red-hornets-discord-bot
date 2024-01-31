import discord
import json


async def server_stats(client, guild_id):
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

    await guild.create_voice_channel(f"MEMBERS: {guild.member_count}", category=new_category)

    print(f'Updated server stats for {guild.name} server')
