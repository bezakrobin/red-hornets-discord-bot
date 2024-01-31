from functions.get_category_by_name import get_category_by_name
from functions.get_channel_containing import get_channel_containing


async def server_stats(client, guild_id):
    guild = client.get_guild(int(guild_id))
    server_stats_category = await get_category_by_name(client, guild_id, '📊 SERVER STATS 📊')
    await server_stats_category.edit(position=0)
    if server_stats_category:
        members_stats_channel = await get_channel_containing(client, guild_id, 'MEMBERS:')
        if members_stats_channel:
            await members_stats_channel.edit(name=f"MEMBERS: {guild.member_count}")
        else:
            members_stats_channel = await guild.create_voice_channel(f'MEMBERS: {guild.member_count}', category=server_stats_category)
    else:
        new_server_stats_category = await guild.create_category('📊 SERVER STATS 📊')
        await new_server_stats_category.edit(position=0)
        members_stats_channel = await guild.create_voice_channel(f'MEMBERS: {guild.member_count}', category=new_server_stats_category)
    print(f'Updated server stats for {guild.name} server')
