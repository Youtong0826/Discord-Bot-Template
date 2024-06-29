import os

from typing import (
    Any,
    Union,
)

from datetime import (
    datetime, 
    timedelta, 
    timezone
)

from discord import (
    Bot, 
    ActionRow,
    SelectMenu,
    Interaction, 
    ComponentType,
    Button as DiscordButton,
    ApplicationContext as AppCtx
)

from discord.ui import (
    View,
    Button,
    Select
)

from dotenv import load_dotenv

load_dotenv()

class Bot(Bot):
    def __init__(self, description=None, *args, **options):
        super().__init__(description, *args, **options)
        self.token = os.getenv("TOKEN")