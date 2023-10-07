import discord
import asyncio
import wavelink
from discord.ext import commands
import json
import settings
from asset.time_convert import milliseconds_to_hh_mm_ss
from Buttons.play_embed_buttons import Music_buttons1
from asset.music_task import my_loop



async def node_connect(bot):
    """
    Connects the bot to a wavelink node.
    """
    # Create a wavelink Node object with the specified URI, password, and secure settings
    node = wavelink.Node(uri=f'{settings.HOST}:{settings.PORT}', password=settings.PASSWORD, secure=settings.SECURE)
    
    # Connect the bot to the node
    await wavelink.NodePool.connect(client=bot, nodes=[node])
    
    # Enable autoplay for wavelink player
    #wavelink.Player.autoplay = True

class Music(commands.Cog):
    def __init__(self, bot:commands.Cog):
        self.bot=bot
        self.myloop = False

    @commands.Cog.listener()
    async def on_ready(self):
        if self.myloop is False:
            await my_loop.start(self.bot)
            self.myloop = True
        else:
            return

    async def cog_load(self):
        print(f'Music Cog has loaded.')
        #await self.load_extension('cog.musico')
        await node_connect(self.bot)        
        
    @commands.Cog.listener()
    async def on_wavelink_track_start(self, payload: wavelink.TrackEventPayload):
        ctx = payload.player.guild
        vc: payload.player = ctx.voice_client
        with open('data.json','r') as f:
            data = json.load(f)
        mch_id = int(data['channel_id'])
        mem_id = int(data['embed_id'])

        m_channel= self.bot.get_channel(mch_id)
        m_embed= await m_channel.fetch_message(mem_id)

        current_track = vc.current
        current_track_duration = await milliseconds_to_hh_mm_ss(current_track.duration)
        position_seconds = vc.position
        duration_seconds = current_track.duration
        progress_percent = (position_seconds / duration_seconds) * 100

        # Create a progress bar using Unicode blocks
        bar_length = 20  # You can adjust the length of the bar
        completed_blocks = int(bar_length * (progress_percent / 100))
        remaining_blocks = bar_length - completed_blocks

        progress_bar = '█' * completed_blocks + '▬' * remaining_blocks

        # Convert position and duration to HH:MM:SS format
        current_time = await milliseconds_to_hh_mm_ss(position_seconds)
        current_track_duration = await milliseconds_to_hh_mm_ss(current_track.duration)
        try:
            queue = f'{vc.queue[0].title}'
        except IndexError:
            queue = 'None'
        
        try:
            thumb=current_track.thumbnail
        except:
            thumb = 'https://images-ext-1.discordapp.net/external/oDIegTXb0iSTvjK5tk757aadM7aQzL2UwP8qCC0SRus/https/cache.lovethispic.com/uploaded_images/310675-Animated-Cat-With-Headphones.gif?width=599&height=449'
        i=0
        list=''
        for songs in vc.queue:
            i=i+1
            list += f'{i}. {songs.title}\n'
        if len(list) == 0:
            list = "Empty"
        updated_em = discord.Embed(title='Playing',
            description=f'{current_track.title}',
            color=discord.Color.random())
        updated_em.set_author(name = f'{self.bot.user.display_name}',
                        icon_url=f'{self.bot.user.display_avatar.url}')
        updated_em.set_thumbnail(url=f'{thumb}')
        updated_em.add_field(name='Coming Up Next', value=f'{queue}')
        updated_em.add_field(name='Volume', value=f"{vc.volume}")
        updated_em.add_field(name='Playing', value=f'[{progress_bar}] {progress_percent:.2f}%', inline=False)
        updated_em.add_field(name=f"{current_time}/{current_track_duration}", value=" ")
        updated_em.add_field(name='Playlist', value=f'{list}',inline=False)

        await m_embed.edit(embed=updated_em, view=Music_buttons1(self.bot))

    @commands.Cog.listener()
    async def on_wavelink_track_end(self, payload: wavelink.TrackEventPayload):
        ctx = payload.player.guild
        vc: wavelink.Player = ctx.voice_client

        if vc.queue.loop is True:
            await vc.play(payload.track)
            return

        else:
            try:
                next_song = vc.queue.get()
                await vc.play(next_song)   
            except:
                with open('data.json','r') as f:
                    data = json.load(f)
                mch_id = int(data['channel_id'])
                m_channel= self.bot.get_channel(mch_id)
                em = discord.Embed(
                    title='Finished',
                    description='The current song or playlist has finished playing.',
                    color=discord.Color.green()
                ) 
                msg=await m_channel.send(embed=em)
                await vc.disconnect()
                await asyncio.sleep(5)
                await msg.delete()
                return
    

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.bot.user:

            with open('data.json','r') as f:
                data = json.load(f)
            mch_id = int(data['channel_id'])
            mem_id = int(data['embed_id'])
            m_channel = message.channel

            if m_channel.id == mch_id:
                song= message.content
            
                await message.delete()
                if not message.author.voice:
                    em = discord.Embed(title='Bruh...',
                        description='Seems that you are not in a voice channel.\nPlease join a voice channel and then search for a song.',
                        color=discord.Color.red())
                    msg = await m_channel.send(embed=em)
                    await asyncio.sleep(5)
                    await msg.delete()

                elif not message.guild.voice_client:

                    vc: wavelink.Player = await message.author.voice.channel.connect(cls = wavelink.Player)
                
            
                vc : wavelink.Player = message.guild.voice_client
                
                search = await wavelink.YouTubeTrack.search(song)
                try:
                    query = search[0]
                    m_embed = await m_channel.fetch_message(mem_id) 

                    if vc.queue.is_empty and not (vc.is_playing()is True or vc.is_paused() is True):
                        
                        time = await milliseconds_to_hh_mm_ss(query.duration)

                        position_seconds = vc.position
                        duration_seconds = query.duration
                        progress_percent = (position_seconds / duration_seconds) * 100

                        # Create a progress bar using Unicode blocks
                        bar_length = 20  # You can adjust the length of the bar
                        completed_blocks = int(bar_length * (progress_percent / 100))
                        remaining_blocks = bar_length - completed_blocks

                        progress_bar = '█' * completed_blocks + '▬' * remaining_blocks

                        # Convert position and duration to HH:MM:SS format
                        current_time = await milliseconds_to_hh_mm_ss(position_seconds)
                        current_track_duration = await milliseconds_to_hh_mm_ss(query.duration)
                    
                        next_song = 'None'

                        em = discord.Embed(title='Playing',
                            description=f'{query.title}',
                            color=discord.Color.green())
                        em.set_author(name = f'{self.bot.user.display_name}',
                                        icon_url=f'{self.bot.user.display_avatar.url}')
                        em.set_thumbnail(url=f'{query.thumbnail}')
                        em.add_field(name='Coming Up Next', value=f'{next_song}')
                        em.add_field(name='Volume', value=f'{vc.volume}')
                        em.add_field(name='Playing', value=f'[{progress_bar}] {progress_percent:.2f}%', inline=False)
                        em.add_field(name=f"{current_time}/{current_track_duration}", value=" ")

                        await m_embed.edit(embed=em, view=Music_buttons1(self.bot))
                        await vc.play(query)
                    else:
                        if vc.channel.id != message.author.voice.channel.id:
                            msg=await m_channel.send(embed=discord.Embed(
                                title='Woah...',
                                description=f"You are not in the same channel as me.\nPlease join {vc.channel.mention} and then use this button.",
                                color=discord.Color.red()
                            ), ephemeral=True)
                            await asyncio.sleep(5)
                            return await msg.delete()
                        else:
                            await vc.queue.put_wait(query)

                            time = await milliseconds_to_hh_mm_ss(query.duration)
                            em = discord.Embed(title='Added to Queue',
                                                description=f'**{query.title} has been added to the queue.**',
                                                color=discord.Color.random())
                            em.add_field(name='Duration', value=f'{time}')
                            em.set_footer(text=f'Requested By | {message.author.display_name}')
                            msg = await m_channel.send(embed=em)
                            await asyncio.sleep(5)
                            await msg.delete()

                            current_track = vc.current
                            current_track_duration = await milliseconds_to_hh_mm_ss(current_track.duration)
                            position_seconds = vc.position
                            duration_seconds = current_track.duration
                            progress_percent = (position_seconds / duration_seconds) * 100

                            # Create a progress bar using Unicode blocks
                            bar_length = 20  # You can adjust the length of the bar
                            completed_blocks = int(bar_length * (progress_percent / 100))
                            remaining_blocks = bar_length - completed_blocks

                            progress_bar = '█' * completed_blocks + '▬' * remaining_blocks

                            # Convert position and duration to HH:MM:SS format
                            current_time = await milliseconds_to_hh_mm_ss(position_seconds)
                            current_track_duration = await milliseconds_to_hh_mm_ss(current_track.duration)
                            try:
                                queue = f'{vc.queue[0].title}'
                            except IndexError:
                                queue = 'None'

                            try:
                                thumb=current_track.thumbnail
                            except:
                                thumb = 'https://images-ext-1.discordapp.net/external/oDIegTXb0iSTvjK5tk757aadM7aQzL2UwP8qCC0SRus/https/cache.lovethispic.com/uploaded_images/310675-Animated-Cat-With-Headphones.gif?width=599&height=449'
            
                            i=0
                            list=''
                            for songs in vc.queue:
                                i=i+1
                                list += f'{i}. {songs.title}\n'
                            if len(list) == 0:
                                list = 'Empty'

                            updated_em = discord.Embed(title='Playing',
                                description=f'{current_track.title}',
                                color=discord.Color.random())
                            updated_em.set_author(name = f'{self.bot.user.display_name}',
                                            icon_url=f'{self.bot.user.display_avatar.url}')
                            updated_em.set_thumbnail(url=f'{thumb}')
                            updated_em.add_field(name='Coming Up Next', value=f'{queue}')
                            updated_em.add_field(name='Volume', value=f'{vc.volume}')
                            updated_em.add_field(name='Playing', value=f'[{progress_bar}] {progress_percent:.2f}%', inline=False)
                            updated_em.add_field(name=f"{current_time}/{current_track_duration}", value=" ")
                            updated_em.add_field(name='Playlist', value=f'{list}',inline=False)

                            await m_embed.edit(embed=updated_em, view=Music_buttons1(self.bot))
                            msg = await m_channel.send(embed=em)
                            await asyncio.sleep(5)
                            await msg.delete()
                except IndexError:
                    msg = await m_channel.send(embed=discord.Embed(title='No Track Found',
                                                    color=discord.Color.red()))
                    await asyncio.sleep(5)
                    await msg.delete()

    @commands.hybrid_command(name="setup")
    async def setup(self, ctx, channel_mention:discord.TextChannel):
        """
        Setup music functionality for your server.
        
        Parameters:
        - channel_mention: The channel you want to setup for music."""
        await ctx.defer()
        # Load channel and embed information from JSON
        try:
            with open('data.json', "r") as f:
                data = json.load(f)

            if data:
                channel_id = int(data["channel_id"])
                embed_id = int(data["embed_id"])

                # Check if the stored channel still exists
                channel = discord.utils.get(ctx.guild.text_channels, id=channel_id)

                if channel:
                    await ctx.send(embed=discord.Embed(title='Music Player is already setup.',
                                                        description=f'You already have a music channel where the bot has been setup.\nPlease delete the {channel.mention} channel and then run this command again.',
                                                        color=discord.Color.yellow()))
                else:
                    # Create and send an embed
                    embed = discord.Embed(title="Setup Embed",
                                        description="This is a setup embed for music bot.\nPlease join a voice channel and type a song or track name in this channel",
                                        color=discord.Color.green())
                    message = await channel_mention.send(embed=embed)

                    # Store channel and embed information in JSON
                    data = {
                        "channel_id": str(channel_mention.id),
                        "embed_id": str(message.id)
                    }
                    with open('data.json', "w") as f:
                        json.dump(data, f)

                    await ctx.send(f"Setup complete in {channel_mention.mention}!")

            else:    
                # Create and send an embed
                embed = discord.Embed(title="Idle",
                                        description="This is a setup embed for music bot.\nPlease join a voice channel and type a song or track name in this channel",
                                        color=discord.Color.green())
                embed.set_footer(text="WARNING | Don't Delete This Message.")
                message = await channel_mention.send(embed=embed)

                # Store channel and embed information in JSON
                data = {
                    "channel_id": str(channel_mention.id),
                    "embed_id": str(message.id)
                }
                with open('data.json', "w") as f:
                    json.dump(data, f)

                await ctx.send(f"Setup complete in {channel_mention.mention}!")
        
        except FileNotFoundError:
            await message.send("No setup data found. Please run the setup command first.")
