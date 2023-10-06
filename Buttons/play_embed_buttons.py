from discord.ext import commands
import discord, wavelink, asyncio
from Buttons.dropdown import Volume

class Music_buttons1(discord.ui.View):
    def __init__(self, bot:commands.Bot):
        super().__init__(timeout=None)
        self.bot = bot
        self.add_item(Volume())

    @discord.ui.button(emoji='⏯️', style=discord.ButtonStyle.blurple)
    async def play(self, interaction: discord.Interaction, button: discord.ui.Button):
        """
        Handles the play button interaction.
        
        Args:
            interaction (discord.Interaction): The interaction object representing the user's interaction.
            button (discord.ui.Button): The play button object.
        """
        await interaction.response.defer(ephemeral=True)
        vc: wavelink.Player = interaction.guild.voice_client

        if not vc:
            # If the bot is not in a voice channel, display an error message
            embed = discord.Embed(
                title="Errr...",
                description="I am not currently playing anything.\nPlease use this command when a song is being played.",
                color=discord.Color.red()
            )
            msg = await interaction.followup.send(embed=embed, ephemeral=True)
            await asyncio.sleep(5)
            return await msg.delete()

        elif not interaction.user.voice:
            # If the user is not in a voice channel, display an error message
            embed = discord.Embed(
                title='Bruh...',
                description='Seems that you are not in a voice channel.\nPlease join a voice channel and then re-run the command.',
                color=discord.Color.red()
            )
            msg = await interaction.followup.send(embed=embed, ephemeral=True)
            await asyncio.sleep(5)
            return await msg.delete()

        elif vc.channel.id != interaction.user.voice.channel.id:
            # If the user is in a different voice channel than the bot, display an error message
            embed = discord.Embed(
                title='Woah...',
                description=f"You are not in the same channel as me.\nPlease join {vc.channel.mention} and then run this command.",
                color=discord.Color.red()
            )
            msg = await interaction.followup.send(embed=embed, ephemeral=True)
            await asyncio.sleep(5)
            return await msg.delete()

        elif vc.is_playing():
            # If the bot is currently playing a song, pause the playback and display a success message
            await vc.pause()
            embed = discord.Embed(
                title='Paused',
                description=f"The song {vc.current.title} has been paused.",
                color=discord.Color.yellow()
            )
            embed.set_footer(text=f'Paused By | {interaction.user.display_name}')
            msg = await interaction.followup.send(embed=embed)
            await asyncio.sleep(5)
            return await msg.delete()

        elif vc.is_paused():
            # If the bot is currently paused, resume the playback and display a success message
            await vc.resume()
            embed = discord.Embed(
                title='▶️ Resumed',
                description=f"The song {vc.current.title} has been resumed.",
                color=discord.Color.red()
            )
            embed.set_footer(text=f'Resumed By | {interaction.user.display_name}')
            msg = await interaction.followup.send(embed=embed)
            await asyncio.sleep(5)
            return await msg.delete()

        elif not vc.is_playing():
            # If no song is currently being played, display a message
            embed = discord.Embed(
                title='Bruh...',
                description="Nothing is being played at the moment.",
                color=discord.Color.yellow()
            )
            msg = await interaction.followup.send(embed=embed, ephemeral=True)
            await asyncio.sleep(5)
            return await msg.delete()

        else:
            # If none of the above conditions are met, display a generic error message
            embed = discord.Embed(
                title='oops...',
                description="Seems some unexpected error occurred. Please tell the creator of the bot.",
                color=discord.Color.red()
            )
            msg = await interaction.followup.send(embed=embed)
            await asyncio.sleep(5)
            return await msg.delete()
        
    @discord.ui.button(emoji='⏹️', style=discord.ButtonStyle.blurple)
    async def stop(self,interaction:discord.Interaction, button:discord.ui.Button):

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
            await vc.disconnect()
            em=discord.Embed(title='⏹️ Music Stopped',
                            description=f'The Music Player has been stopped.',
                            color=discord.Color.green())
            em.set_author(name=f'Requested By | {interaction.user.display_name}')
            msg=await interaction.followup.send(embed=em)
            await asyncio.sleep(5)
            return await msg.delete()
        

    @discord.ui.button(emoji='⏭️', style=discord.ButtonStyle.blurple)
    async def skip(self,interaction:discord.Interaction, button:discord.ui.Button):

        await interaction.response.defer()
        vc: wavelink.Player = interaction.guild.voice_client

        if not interaction.guild.voice_client:
            Embed= discord.Embed(title="Errr...",
                                description="I am not currently playing anything.\nPlease use this button when a song is being played.",
                                color=discord.Color.red())
            msg=await interaction.followup.send(embed=Embed,ephemeral=True)
            await asyncio.sleep(5)
            return await msg.delete()
        # Check if the user is not in a voice channel
        elif not interaction.user.voice:
            # Send a reply to the user indicating they need to join a voice channel
            msg=await interaction.followup.send(embed=discord.Embed(
                title='Bruh...',
                description='Seems that you are not in a voice channel.\nPlease join a voice channel and then press the button.',
                color=discord.Color.red()
            ), ephemeral=True)
            await asyncio.sleep(5)
            return await msg.delete()
        
        elif vc.channel.id != interaction.user.voice.channel.id:
            # If the author is in a different voice channel than the bot, display an error message
            msg= await interaction.followup.send(embed=discord.Embed(
                title='Woah...',
                description=f"You are not the same channel as me.\nPlease join {vc.channel.mention} and then run this command.",
                color=discord.Color.red()
            ), ephemeral= True)
            await asyncio.sleep(5)
            return await msg.delete()
        else:
            # Stop the playback in the voice channel
            await vc.stop()
            
            # Create an embed message to indicate that the song was skipped
            embed = discord.Embed(
                title='⏭️ Skipped',
                description=f"The song {vc.current.title} was skipped.",
                color=discord.Color.green()
            )
            embed.set_footer(text=f"Requested By | {interaction.user.display_name}")
            
            # Send the embed message to the channel
            msg=await interaction.followup.send(embed=embed)
            await asyncio.sleep(5)
            return await msg.delete()
    
    @discord.ui.button(emoji='🔁', style=discord.ButtonStyle.blurple)
    async def loop_song(self,interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.defer()
        vc: wavelink.Player = interaction.guild.voice_client

        if not interaction.guild.voice_client:
            Embed= discord.Embed(title="Errr...",
                                description="I am not currently playing anything.\nPlease use this button when a song is being played.",
                                color=discord.Color.red())
            msg=await interaction.followup.send(embed=Embed,ephemeral=True)
            await asyncio.sleep(5)
            return await msg.delete()
        # Check if the user is not in a voice channel
        elif not interaction.user.voice:
            # Send a reply to the user indicating they need to join a voice channel
            msg=await interaction.followup.send(embed=discord.Embed(
                title='Bruh...',
                description='Seems that you are not in a voice channel.\nPlease join a voice channel and then press the button.',
                color=discord.Color.red()
            ), ephemeral=True)
            await asyncio.sleep(5)
            return await msg.delete()
        
        elif vc.channel.id != interaction.user.voice.channel.id:
            # If the author is in a different voice channel than the bot, display an error message
            msg= await interaction.followup.send(embed=discord.Embed(
                title='Woah...',
                description=f"You are not the same channel as me.\nPlease join {vc.channel.mention} and then run this command.",
                color=discord.Color.red()
            ), ephemeral= True)
            await asyncio.sleep(5)
            return await msg.delete()
        else:
            if vc.is_playing() == True or vc.is_paused()==True:

                if vc.queue.loop == False:
                    vc.queue.loop = True
                    em = discord.Embed(
                    title='Loop Enabled',
                    description='The current Song has been put on loop.',
                    color=discord.Color.red()
                    )
                    em.set_footer(text=f'Requested By | {interaction.user.display_name}')
                    msg=await interaction.followup.send(embed=em)
                    await asyncio.sleep(5)
                    return await msg.delete()
                
                elif vc.queue.loop == True:
                    vc.queue.loop = False
                    em = discord.Embed(
                    title='Loop Disabled',
                    description='The loop has been disabled.',
                    color=discord.Color.red()
                    )
                    em.set_footer(text=f'Requested By | {interaction.user.display_name}')
                    msg=await interaction.followup.send(embed=em)
                    await asyncio.sleep(5)
                    return await msg.delete()
            