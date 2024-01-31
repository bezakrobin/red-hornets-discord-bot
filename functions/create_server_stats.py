from load_data import load_data
from delete_category_and_channels import delete_category_and_channels
from create_locked_channel import create_locked_channel
from create_category import create_category
from save_data import save_data


async def create_server_stats(guild_id, client):
    data = load_data()
    if data['service_stats_category'] != 0:
        category_to_delete = client.get_channel(int(data['service_stats_category']))
        await delete_category_and_channels(category_to_delete)
    guild = client.get_guild(int(guild_id))
    category = await create_category(guild, '📊 SERVER STATS 📊', 0)
    data['server_stats_category'] = category.id
    save_data(data)
    await create_locked_channel(guild, f"MEMBERS: {data['member_count']}", 'voice', category)
    await create_locked_channel(guild, f"SUGGESTIONS: {data['suggestions_count']}", 'voice', category)
    await create_locked_channel(guild, f"SUGGESTIONS DONE: {data['suggestions_done_count']}", 'voice', category)
    await create_locked_channel(guild, f"BUGS: {data['bugs_count']}", 'voice', category)
    await create_locked_channel(guild, f"BUGS FIXED: {data['bugs_fixed_count']}", 'voice', category)
