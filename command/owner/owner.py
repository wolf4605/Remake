import discord
from discord.ext import commands


class Owner(commands.Cog):
    """A Cog Class that contains functions that are only for the use of bot owner"""
    def __init__(self, bot):
        """Initializes a new instance of the class."""
        self.bot = bot
        
    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx):
        """A command that synchronizes the bot's tree."""
        
        synced= await self.bot.tree.sync()
        await ctx.send(f"Synced {len(synced)} commands")
    