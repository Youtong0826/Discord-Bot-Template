from lib.cog import CogExtension
from core import Bot

from discord import (
    ApplicationContext,
    slash_command,
)

from discord.utils import find

class ExampleCommands(CogExtension):
    @slash_command()
    async def say(self, ctx: ApplicationContext, *, msg: str):
        await ctx.send(msg)
        
def setup(bot: Bot):
    bot.add_cog(ExampleCommands(bot))