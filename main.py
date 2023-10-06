import discord
import wavelink
import settings
import logging
import os
from discord.ext import commands
from asset import color

log = logging.FileHandler(filename='Logs.txt', encoding='utf-8',mode='w')
class Mew(commands.Bot):
    """Main BOT class"""
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.presences = True
        intents.members = True
        super().__init__(command_prefix=settings.Prefix, intents=intents)

    async def setup_hook(self):
        try:
            for filename in os.listdir("command"):
                if '.py' not in filename:
                    print(f'{color.YELLOW}{filename} is a folder!!!')
                else:
                    await bot.load_extension(f'command.{filename[:-3]}')
                    print(f'{color.GREEN}{filename} has been loaded.')
            print(f'{color.CYAN} Inititalizing...')

        except Exception as e:
            print(e)         
            raise

bot = Mew()

@bot.listen()
async def on_ready():
    """
    Function called when the bot is ready to start receiving events.
    """
    print(f'Logged in as {bot.user}.')

@bot.listen()
async def on_wavelink_node_ready(node: wavelink.Node):
    """
    Called when a Wavelink node is ready.
    
    Parameters:
        node (wavelink.Node): The Wavelink node that is ready.
    """
    # Print a message indicating that the node has successfully connected
    print(f'Node : {node.id} successfully connected.')

bot.run(token=settings.Token, log_handler=log, log_level=logging.DEBUG, root_logger=True)
