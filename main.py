import discord
from discord.ext import commands
import settings

print (settings.Prefix)
class Mew(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=settings.PREFIX, intents=intents)