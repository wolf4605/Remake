import discord
import wavelink
import asyncio

class Volume(discord.ui.Select):
    def __init__(self):

        # Set the options that will be presented inside the dropdown
        options = [
            discord.SelectOption(label='10',value='10'),
            discord.SelectOption(label='20',value='20'),
            discord.SelectOption(label='30',value='30'),
            discord.SelectOption(label='40',value='40'),
            discord.SelectOption(label='50',value='50'),
            discord.SelectOption(label='60',value='60'),
            discord.SelectOption(label='70',value='70'),
            discord.SelectOption(label='80',value='80'),
            discord.SelectOption(label='90',value='90',),
            discord.SelectOption(label='100',value='100'),
        ]

        super().__init__(placeholder='Select Volume', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        # Get the voice client in the current guild
        vc: wavelink.Player = interaction.guild.voice_client

        # If the bot is not currently playing anything
        if not vc:
            # Create an embed message to notify the user
            embed = discord.Embed(
                title="Errr...",
                description="I am not currently playing anything.\nPlease use this button when a song is being played.",
                color=discord.Color.red()
            )
            msg=await interaction.followup.send(embed=embed, ephemeral=True)
            await asyncio.sleep(5)
            return await msg.delete()
        # If the user is not in a voice channel
        elif not interaction.user.voice:
            # Create an embed message to notify the user
            msg= await interaction.followup.send(embed=discord.Embed(
                title='Bruh...',
                description='Seems that you are not in a voice channel.\nPlease join a voice channel and then press the button.',
                color=discord.Color.red()
            ), ephemeral=True)
            await asyncio.sleep(5)
            return await msg.delete()

        # If the user is in a different voice channel than the bot
        elif vc.channel.id != interaction.user.voice.channel.id:
            # Create an embed message to notify the user
            msg=await interaction.followup.send(embed=discord.Embed(
                title='Woah...',
                description=f"You are not in the same channel as me.\nPlease join {vc.channel.mention} and then use this button.",
                color=discord.Color.red()
            ), ephemeral=True)
            await asyncio.sleep(5)
            return await msg.delete()
        #  If the user is in the same voice channel than the bot
        elif vc.channel.id == interaction.user.voice.channel.id:
            await vc.set_volume(int(self.values[0]))
            em=discord.Embed(title='Volume Set',
                            description=f'The Volume has been set to {self.values[0]}%.',
                            color=discord.Color.green())
            em.set_author(name=f'Requested By | {interaction.user.display_name}')
            msg=await interaction.followup.send(embed=em)
            await asyncio.sleep(5)
            return await msg.delete()
