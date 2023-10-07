import discord
from discord.ext import commands
from command.fun_commands.FUN_1 import Fun_Commands
from command.music.music import Music
from command.anon.anonymous import Anonymous
from command.level.leveling import Leveling
from command.owner.owner import Owner

async def setup(bot:commands.Bot):
    await bot.add_cog(Fun_Commands(bot))
    await bot.add_cog(Anonymous(bot))
    await bot.add_cog(Owner(bot))
    await bot.add_cog(Leveling(bot))
    await bot.add_cog(Music(bot))
