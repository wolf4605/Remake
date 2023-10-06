import discord, os
from discord.ext import commands
import aiohttp
import random
import settings
from asset.send_webhook import send_message


anon = settings.ANONYMUS_CHANNEL



class Anonymous(commands.Cog):
    """Talk in the anonymous channel where know one knows who is who.\nHave fun guessing the anonymous sender.\n"""
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or message.webhook_id:
            return

    # Check if the message is in the desired channel
        if message.channel.id == anon:
        # Delete the message
            await message.delete()
        
        # Send an ephemeral response
            ephemeral_msg = await message.channel.send("Please Use **/send** to send a message in this channel.", delete_after=5)

        else:
            return

    # The Command
    @commands.hybrid_command()
    async def send(self,ctx, *, content):
        """Send an anonymous message in the anonymous Channel"""
        await ctx.defer(ephemeral=True)
        if "@everyone" in content or "@here" in content or any(member.mention in content for member in ctx.guild.members) or any(role.mention in content for role in ctx.guild.roles):
            await ctx.send("You cannot ping anyone in the message for anonymous chat.", ephemeral=True)
        else:
            try:
        	    await ctx.send("Message sent", ephemeral=True)
        	    await send_message(content)
            except Exception as e:
                await ctx.send(f'An error occured. Please try again.\nIf the error still happens.\n\nPlease send this codeblock to the bot owner ```{e}```')

    
    
async def setup(bot:commands.Bot):
    await bot.add_cog(Anonymous(bot))

