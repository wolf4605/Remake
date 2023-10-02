import discord
import settings
import logging
import os
from discord.ext import commands
from asset import color

log = logging.FileHandler(filename='Logs.txt', encoding='utf-8',mode='w')
class Mew(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=settings.Prefix, intents=intents)

    async def setup_hook(self):
        for filename in os.listdir("commands"):
            await bot.load_extension(f'commands.{filename[:-3]}')
        print(f'{color.BOLD}{color.RED} Starting')

bot = Mew()

@bot.listen()
async def on_ready():
    """
    Function called when the bot is ready to start receiving events.
    
    Parameters:
        None
    
    Returns:
        None
    """
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

bot.run(token=settings.Token, log_handler=log, log_level=logging.DEBUG, root_logger=True)
