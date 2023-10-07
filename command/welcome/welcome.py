import discord
import asyncio
from discord.ext import commands
import settings
class Welcome(commands.Cog):
    """Resposible For Welcoming New Members"""
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(settings.WELCOME_CHANNEL)
        #if you want to message more message then you can add like this
        await channel.send(embed=discord.Embed(title="🎊 Welcome 🎊",
                                            color=random.randint(0,0xFFFFFF),
        description=f"<a:sparkling:990720256580386896><a:Bouncy_nya:990722989203021854><a:moon_stars:1064538162518564874> Hey {member.mention} has just joined the cafe!  Hope you have a pawsome time in MoonLightNekos !! <a:moon_stars:1064538162518564874><a:Bouncy_nya:990722989203021854><a:sparkling:990720256580386896>\n━━━━━━━━━━━━━━ ⋆⋅ ☾ ⋅⋆ ━━━━━━━━━━━━━━\n<a:Pastel_Moon:1064529200238833674> Choose a color for your name in <#990733298730934322> channel\n<a:Pastel_Moon:1064529200238833674> You may also gain special role access in <#990730814855712818>\n<a:Pastel_Moon:1064529200238833674> And if you play Toram Online...Tell us briefly of yourself here in <#1008904966590697615> ! We would appreciate it very much (⁠╹⁠▽⁠╹⁠⁠) /"
        ))
        
        #for sending the card
        await channel.send(file=file)
        #Nothing
