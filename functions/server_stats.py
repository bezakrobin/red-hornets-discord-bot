import discord
from functions.load_value_from_json import load_value_from_json
from functions.save_value_to_json import save_value_to_json


async def server_stats(client, guild_id):
    server_stats_category = load_value_from_json('server_stats_category')
    server_stats_members_channel = load_value_from_json('server_stats_members_channel')
    guild = client.get_guild(int(guild_id))
    save_value_to_json('server_stats_member_count', guild.member_count)
    if server_stats_members_channel is None:
        if server_stats_category:
            category = discord.utils.get(guild.categories, id=int(server_stats_category))
            if category:
                for channel in category.channels:
                    await channel.delete()
                await category.delete()
        new_server_stats_category = await guild.create_category('📊 SERVER STATS 📊')
        await new_server_stats_category.edit(position=0)
        save_value_to_json('server_stats_category', new_server_stats_category.id)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(connect=False)
        }
        server_stats_members_channel = await guild.create_voice_channel(f"MEMBERS: {load_value_from_json('server_stats_member_count')}", category=new_server_stats_category, overwrites=overwrites)
        save_value_to_json('server_stats_members_channel', server_stats_members_channel.id)
    else:
        server_stats_members_channel = client.get_channel(server_stats_members_channel)
        await server_stats_members_channel.edit(name=f"MEMBERS: {load_value_from_json('server_stats_member_count')}")
    print(f'Updated server stats for {guild.name} server')
