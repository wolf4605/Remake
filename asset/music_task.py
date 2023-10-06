import discord
import wavelink
from discord.ext import tasks
import json
from asset.time_convert import milliseconds_to_hh_mm_ss
from Buttons.play_embed_buttons import Music_buttons1

@tasks.loop(seconds=30.0,reconnect=True,count=None)
async def my_loop(bot):
    try:
        with open('data.json','r') as f:
            data = json.load(f)
        mch_id = int(data['channel_id'])
        mem_id = int(data['embed_id'])

        m_channel= bot.get_channel(mch_id)
        m_embed= await m_channel.fetch_message(mem_id)

        guild = m_channel.guild
        vc:wavelink.Player = guild.voice_client
        if not guild.voice_client:
            updated_em = discord.Embed(title='Idle',
                                    description="I'm not busy at the moment.\nPlease type the name of a song or paste a youtube link.",
                                    color=discord.Color.random() )
            updated_em.set_author(name = f'{bot.user.display_name}',
                            icon_url=f'{bot.user.display_avatar.url}')
            updated_em.set_footer(text="WARNING | Don't Delete This Message.")
            await m_embed.edit(embed=updated_em)

        elif vc.is_playing():
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
            updated_em.set_author(name = f'{bot.user.display_name}',
                            icon_url=f'{bot.user.display_avatar.url}')
            updated_em.set_thumbnail(url=f'{thumb}')
            updated_em.add_field(name='Coming Up Next', value=f'{queue}')
            updated_em.add_field(name='Volume', value=f'{vc.volume}')
            updated_em.add_field(name='Playing', value=f'[{progress_bar}] {progress_percent:.2f}%', inline=False)
            updated_em.add_field(name=f"{current_time}/{current_track_duration}", value=" ")
            updated_em.add_field(name='Playlist', value=f'{list}',inline=False)

            await m_embed.edit(embed=updated_em, view=Music_buttons1(bot))
        elif vc.is_paused():
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
            updated_em = discord.Embed(title='Paused',
                description=f'{current_track.title}',
                color=discord.Color.random())
            updated_em.set_author(name = f'{bot.user.display_name}',
                            icon_url=f'{bot.user.display_avatar.url}')
            updated_em.set_thumbnail(url=f'{thumb}')
            updated_em.add_field(name='Coming Up Next', value=f'{queue}')
            updated_em.add_field(name='Volume', value=f'{vc.volume}')
            updated_em.add_field(name='Playing', value=f'[{progress_bar}] {progress_percent:.2f}%', inline=False)
            updated_em.add_field(name=f"{current_time}/{current_track_duration}", value=" ")
            updated_em.add_field(name='Playlist', value=f'{list}',inline=False)
            

            await m_embed.edit(embed=updated_em, view=Music_buttons1(bot))
    except:
        print("Music Cog Not Setup.")