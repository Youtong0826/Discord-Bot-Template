from lib.cog import CogExtension
from core import Bot

from discord import (
    Cog,
    Member
)

class ExampleEvents(CogExtension):
    @Cog.listener()
    async def on_member_join(self, member: Member):
        self.bot.log("new member join:", member.name, "id:", member.id)
        
def setup(bot: Bot):
    bot.add_cog(ExampleEvents(bot))