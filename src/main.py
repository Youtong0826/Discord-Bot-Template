import os
import sys
import discord

from dotenv import load_dotenv
from core import Bot

load_dotenv()

bot = Bot(
    intents = discord.Intents.all(),
    command_prefix = "!"
)

@bot.event
async def on_ready():
    print("bot is ready!!")
    print("python version:", sys.version[0:9]) 
    print("pycord version:", discord.__version__[0:5])

if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))