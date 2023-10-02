import discord
from discord.ext import commands


print (configurations.Prefix)
class Mew(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=configurations.PREFIX, intents=intents)