import discord
import random
from discord.ext import commands
from asset import image_links

class FUN1(commands.Cog):
    '''Class for bot command'''
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def bite(self, ctx:commands.Context, member:discord.Member):
        """
        Sends a bite animation to the specified member.
        
        Parameters:
        - ctx (commands.Context): The context of the command.
        - member (discord.Member): The member to bite.
        """

        await ctx.defer()

        # Choose a random bite animation image
        image = random.choice(image_links.BITE)

        # List of possible phrases for the embed
        phrases = [
            f"{ctx.author.display_name} is nibbling {member.display_name} !",
            f"{ctx.author.display_name} is biting {member.display_name} ! Owie...",
            f"{ctx.author.display_name} has bitten {member.display_name} !!",
            f"{ctx.author.display_name} is biting {member.display_name} ! That must have hurt...",
        ]
        
        # Choose a random phrase
        phrase = random.choice(phrases)

        # Create an embed with the bite animation and phrase
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=phrase, icon_url=ctx.author.display_avatar)
        embed.set_image(url=image)

        # Send the embed
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def brokiss(self, ctx, member):

        await ctx.defer()

        # Choose a random brokiss image
        image = random.choice(image_links.BRO_KISS)

        # List of possible phrases for the embed
        phrases= []

        # Choose a random phrase
        phrase = random.choice(phrases)

        # Create an embed with the brokiss animation and phrase
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=phrase, icon_url=ctx.author.display_avatar)
        embed.set_image(url=image)

        # Send the embed
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def galkiss(self, ctx, member):

        await ctx.defer()

        # Choose a random galkiss image
        image = random.choice(image_links.GIRL_KISS)

        # List of possible phrases for the embed
        phrases= [f"{ctx.author.display_name} kisses {member.display_name} ～ 💖 ",
                f"{ctx.author.display_name} smooches {member.display_name} !! How cute～",
                f"{ctx.author.display_name} kisses {member.display_name}!! Muwaaah",
                f"{ctx.author.display_name} kisses {member.display_name}!!! Things are heating up...",
                ]

        # Choose a random phrase
        phrase = random.choice(phrases)

        # Create an embed with the galkiss animation and phrase
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=phrase, icon_url=ctx.author.display_avatar)
        embed.set_image(url=image)

        # Send the embed
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def hug(self, ctx, member):

        await ctx.defer()

        # Choose a random Hug image
        image = random.choice(image_links.HUG)

        # List of possible phrases for the embed
        phrases= [f"{ctx.author.display_name} hugged {member.display_name}!!! UwU",
                f"{ctx.author.display_name} gives {member.display_name} a big bear hug !!",
                f"{ctx.author.display_name} warmly hugs {member.display_name}. Aww~",
                f"{ctx.author.display_name} cuddles {member.display_name}!!!",
                f"{ctx.author.display_name} squeezes {member.display_name}!!!",
                ]

        # Choose a random phrase
        phrase = random.choice(phrases)

        # Create an embed with the Hug animation and phrase
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=phrase, icon_url=ctx.author.display_avatar)
        embed.set_image(url=image)

        # Send the embed
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def kick(self, ctx, member):

        await ctx.defer()

        # Choose a random kick image
        image = random.choice(image_links.KICK)

        # List of possible phrases for the embed
        phrases = [f"{ctx.author.display_name} lands a perfect kick at {member.display_name}, looks painful",
                f"{ctx.author.display_name} slam kicks {member.display_name}!! Ouch...",
                f"Watch out, {ctx.author.display_name} is kicking {member.display_name}!!!",
                f"{ctx.author.display_name} kicks {member.display_name}!",
                ]

        # Choose a random phrase
        phrase = random.choice(phrases)

        # Create an embed with the kick animation and phrase
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=phrase, icon_url=ctx.author.display_avatar)
        embed.set_image(url=image)

        # Send the embed
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def kill(self, ctx, member):

        await ctx.defer()

        # Choose a random kill image
        image = random.choice(image_links.KILL)

        # List of possible phrases for the embed
        phrases= [f"{ctx.author.display_name} completely obliterates {member.display_name} to death!",
                f"{ctx.author.display_name} brutally murders {member.display_name}!! 💀",
                f"{ctx.author.display_name} murdered {member.display_name}!!! Brutal",
                f"{ctx.author.display_name} eliminates {member.display_name} out of existence !!!",
                f"{ctx.author.display_name} annihilates {member.display_name} !! Poor them...",
                ]

        # Choose a random phrase
        phrase = random.choice(phrases)

        # Create an embed with the kill animation and phrase
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=phrase, icon_url=ctx.author.display_avatar)
        embed.set_image(url=image)

        # Send the embed
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def kiss(self, ctx, member):

        await ctx.defer()

        # Choose a random kiss image
        image = random.choice(image_links.KISS)

        # List of possible phrases for the embed
        phrases= [f"{ctx.author.display_name} kisses {member.display_name} ～ 💖 ",
                f"{ctx.author.display_name} smooches {member.display_name} !! How cute～",
                f"{ctx.author.display_name} kisses {member.display_name}!! Muwaaah",
                f"{ctx.author.display_name} kisses {member.display_name}!!! Things are heating up...",
                ]

        # Choose a random phrase
        phrase = random.choice(phrases)

        # Create an embed with the kiss animation and phrase
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=phrase, icon_url=ctx.author.display_avatar)
        embed.set_image(url=image)

        # Send the embed
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def laugh(self, ctx, member):

        await ctx.defer()

        # Choose a random laugh image
        image = random.choice(image_links.LAUGH)

        # List of possible phrases for the embed
        phrases= [f"{ctx.author.display_name} giggles at {member.display_name} !!!",
                f"{ctx.author.display_name} is laughing at {member.display_name} 😂 ",
                f"{ctx.author.display_name} finds {member.display_name} quite hilarious! ",
                f"{ctx.author.display_name} is rolling on the floor laughing at {member.display_name}!!! 🤣 ",
                ]

        # Choose a random phrase
        phrase = random.choice(phrases)

        # Create an embed with the laugh animation and phrase
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=phrase, icon_url=ctx.author.display_avatar)
        embed.set_image(url=image)

        # Send the embed
        await ctx.send(embed=embed)

    @commands.hybrid_command(aliases=['pet'])
    async def pat(self, ctx, member):

        await ctx.defer()

        # Choose a random patting image
        image = random.choice(image_links.PAT)

        # List of possible phrases for the embed
        phrases= [f"{ctx.author.display_name} is petting {member.display_name}",
                f"{member.display_name}, you have been patted by {ctx.author.display_name} !",
                f"{ctx.author.display_name} pats {member.display_name} gently",
                f"{ctx.author.display_name} pets {member.display_name}'s head ! Adorable ! 💕 ",
                ]

        # Choose a random phrase
        phrase = random.choice(phrases)

        # Create an embed with the patting animation and phrase
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=phrase, icon_url=ctx.author.display_avatar)
        embed.set_image(url=image)

        # Send the embed
        await ctx.send(embed=embed)