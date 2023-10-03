import discord
from discord.ext import commands
from command.fun_commands.FUN_1 import Fun_Commands

async def setup(bot:commands.Bot):
    await bot.add_cog(Fun_Commands(bot))