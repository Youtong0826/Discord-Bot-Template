from discord import Cog, Bot

class CogExtension(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot