class VoiceChannel:
    def __init__(self, name):
        self.name = name


class TextChannel:
    def __init__(self, name):
        self.name = name


class Category:
    def __init__(self, name, channels=None):
        self.name = name
        self.channels = channels if channels is not None else []


async def structures():
    category1 = Category("📊 SERVER STATS 📊", [VoiceChannel("👥")])
    category2 = Category("💡 SUGGESTIONS STATS 💡", [VoiceChannel("✍️"), VoiceChannel("⚒️"), VoiceChannel("✅"), VoiceChannel("⛔")])
    category3 = Category("🪲 BUGS STATS 🪲", [VoiceChannel("✍️"), VoiceChannel("⚒️"), VoiceChannel("✅"), VoiceChannel("⛔")])

    return [category1, category2, category3]
