import discord
from discord.ext import commands
import random
from asset import image_links

class FUN2(commands.Cog):
    '''Class for bot command'''
    def __init__(self, bot):
        self.bot = bot    
    
    @commands.hybrid_command()
    async def poke(self, ctx, member:discord.Member):
        """
        Poke someone but in the right place.
        
        Parameters:
        - ctx (discord.ext.commands.Context): The context of the command.
        - member: The member to poke.
        """

        await ctx.defer()

        # Choose a random poke image
        image = random.choice(image_links.POKE)

        # List of possible phrases for the embed
        phrases= [f"{ctx.author.display_name} poked {member.display_name}...",
                   f"{ctx.author.display_name} just poked {member.display_name}!!!"
                ]

        # Choose a random phrase
        phrase = random.choice(phrases)

        # Create an embed with the Poke animation and phrase
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=phrase, icon_url=ctx.author.display_avatar)
        embed.set_image(url=image)

        # Send the embed
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def pout(self, ctx):
        """
        Ever tried pouting yourself.
        
        Parameters:
        - ctx (discord.ext.commands.Context): The context of the command.
        """
        await ctx.defer()

        # Choose a random pout image
        image = random.choice(image_links.POUT)

        # List of possible phrases for the embed
        phrases= [f"{ctx.author.display_name} just pouted!!! awww~~~😊",
                f"{ctx.author.display_name} pouted~~Kawaii~~"
                ]

        # Choose a random phrase
        phrase = random.choice(phrases)

        # Create an embed with the pout animation and phrase
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=phrase, icon_url=ctx.author.display_avatar)
        embed.set_image(url=image)

        # Send the embed
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def punch(self, ctx, member:discord.Member):
        """
        You want me to explain this too. Seriously!
        
        Parameters:
        - ctx (discord.ext.commands.Context): The context of the command.
        - member: The member to punch.
        """
        await ctx.defer()

        # Choose a random punch image
        image = random.choice(image_links.PUNCH)

        # List of possible phrases for the embed
        phrases= [f"{ctx.author.display_name} punched {member.display_name}!!! In you face 👊.",
               f"{ctx.author.display_name} punched {member.display_name}!!! You can't see me 🖐️.",
                ]

        # Choose a random phrase
        phrase = random.choice(phrases)

        # Create an embed with the Punch animation and phrase
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=phrase, icon_url=ctx.author.display_avatar)
        embed.set_image(url=image)

        # Send the embed
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def rip(self, ctx):
        """
        REST IN PEACE
        
        Parameters:
        - ctx (discord.ext.commands.Context): The context of the command.
        """

        await ctx.defer()

        # Choose a random rip image
        image = random.choice(image_links.RIP)

        # List of possible phrases for the embed
        phrases= [f"{ctx.author.display_name} died a lonely death 💀",
                   f"{ctx.author.display_name}... 🪦 RIP",
                   f"May {ctx.author.display_name} rest peacefully",
                   f"{ctx.author.display_name} died!! One more weight off this world 💀",
                ]

        # Choose a random phrase
        phrase = random.choice(phrases)

        # Create an embed with the rip animation and phrase
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=phrase, icon_url=ctx.author.display_avatar)
        embed.set_image(url=image)

        # Send the embed
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def slap(self, ctx, member:discord.Member):
        """
        Time to slap some bish.
        
        Parameters:
        
        - ctx (discord.ext.commands.Context): The context of the command.
        - member: The bish to slap."""

        await ctx.defer()

        # Choose a random slap image
        image = random.choice(image_links.SLAP)

        # List of possible phrases for the embed
        phrases= [f"{ctx.author.display_name} is slapping {member.display_name}!!",
                f"{ctx.author.display_name} slapped {member.display_name}",
                f"{ctx.author.display_name} has slapped {member.display_name}. Ouchies",
                f"{ctx.author.display_name} slaps {member.display_name} out of existance !!!",
                ]

        # Choose a random phrase
        phrase = random.choice(phrases)

        # Create an embed with the slap animation and phrase
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=phrase, icon_url=ctx.author.display_avatar)
        embed.set_image(url=image)

        # Send the embed
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def smug(self, ctx, member:discord.Member):
        """
        Even I don't know what smug is.
        
        Parameters:
        - ctx (discord.ext.commands.Context): The context of the command.
        - member: The member to smug at."""
        await ctx.defer()

        # Choose a random smug image
        image = random.choice(image_links.SMUG)

        # List of possible phrases for the embed
        phrases= [f"{ctx.author.display_name} makes a smug face at {member.display_name} !",
                   f"{ctx.author.display_name} conceitedly smugs at {member.display_name} !! 🤭 ",
                ]

        # Choose a random phrase
        phrase = random.choice(phrases)

        # Create an embed with the smug animation and phrase
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=phrase, icon_url=ctx.author.display_avatar)
        embed.set_image(url=image)

        # Send the embed
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def spank(self, ctx, member:discord.Member):
        """
        Everyone loves spanking. Right?
        
        Parameters:
        - ctx (discord.ext.commands.Context): The context of the command.
        - member: The member to spank.
        """
        await ctx.defer()

        # Choose a random spank image
        image = random.choice(image_links.SPANK)

        # List of possible phrases for the embed
        phrases= [f"{ctx.author.display_name} spanks {member.display_name} ! How naughty 〜",
                f"{ctx.author.display_name} spanks {member.display_name}'s butt !! Oh my 〜 !!",
                f"{ctx.author.display_name} spanked {member.display_name} 〜 kinky...",
                ]

        # Choose a random phrase
        phrase = random.choice(phrases)

        # Create an embed with the spank animation and phrase
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=phrase, icon_url=ctx.author.display_avatar)
        embed.set_image(url=image)

        # Send the embed
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def stare(self, ctx):
        """
        Stare at something.
        
        Parameters:
        - ctx (discord.ext.commands.Context): The context of the command.
        """

        await ctx.defer()

        # Choose a random stare image
        image = random.choice(image_links.BRO_KISS)

        # List of possible phrases for the embed
        phrases= [f"{ctx.author.display_name} is staring at something.",
                   f"{ctx.author.display_name} is staring some body must have felt a chill.",
                   f"{ctx.author.display_name} is observing.",
                ]

        # Choose a random phrase
        phrase = random.choice(phrases)

        # Create an embed with the stare animation and phrase
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=phrase, icon_url=ctx.author.display_avatar)
        embed.set_image(url=image)

        # Send the embed
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def tickle(self, ctx, member:discord.Member):
        """
        Who wants to be tickled??
        
        Parameters:
        - ctx (discord.ext.commands.Context): The context of the command.
        - member: The member to tickle.
        """
        await ctx.defer()

        # Choose a random tickle image
        image = random.choice(image_links.BRO_KISS)

        # List of possible phrases for the embed
        phrases= [f"{ctx.author.display_name} tickled {member.display_name}!!! hehehe",
                   f"{ctx.author.display_name} is tickling {member.display_name}!!! tickle tickle tickle",
                ]

        # Choose a random phrase
        phrase = random.choice(phrases)

        # Create an embed with the tickle animation and phrase
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=phrase, icon_url=ctx.author.display_avatar)
        embed.set_image(url=image)

        # Send the embed
        await ctx.send(embed=embed)
        