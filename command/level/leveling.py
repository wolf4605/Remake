import discord, aiosqlite, asyncio
from discord.ext import commands
import settings

role_names = settings.Level_Roles
role_levels = settings.Level_Num
prefix = settings.Prefix
admin = settings.Moderator_Role


class Leveling(commands.Cog):
    """I have a leveling system too."""
    def __init__(self,bot:commands.Bot):
        self.bot=bot
    @commands.Cog.listener()
    async def on_ready(self):
        pass

    async def cog_load(self):
        try:
            self.bot.db=await aiosqlite.connect('leveling.db')
            cursor = await self.bot.db.cursor()

            # Create a table to store leveling data if it doesn't exist
            await cursor.execute('''CREATE TABLE IF NOT EXISTS leveling (
                                guild_id INTEGER,
                                user_id INTEGER,
                                level INTEGER,
                                xp INTEGER,
                                messages INTEGER,
                                PRIMARY KEY (guild_id, user_id)
                            )''')
            await self.bot.db.commit()
        except Exception as e:
            print(e)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        async with aiosqlite.connect("leveling.db") as conn:
            await conn.execute(
                "DELETE FROM leveling WHERE guild_id = ? AND user_id = ?",
                (member.guild.id, member.id),
            )
            await conn.commit()
        
        print(f"{member.display_name}'s data has been deleted.")

    @commands.Cog.listener()
    async def on_message(self, message):
        # the bot's prefix is ! that's why we are adding this statement so user's xp doesn't increase when they use any commands
        if not message.content.startswith(prefix):

            # checking if the bot has not sent the message
            if not message.author.bot:
                # Check if the message is from a guild (server)
                if message.guild:
                    # Get the user's leveling data
                    cursor = await self.bot.db.cursor()
                    await cursor.execute('SELECT * FROM leveling WHERE guild_id = ? AND user_id = ?', (message.guild.id, message.author.id))
                    data = await cursor.fetchone()

                    if data is None:
                        # If the user is not in the database, add them with initial values
                        await cursor.execute('INSERT INTO leveling VALUES (?, ?, 0, 0, 1)', (message.guild.id, message.author.id))
                    else:
                        # If the user is in the database, update their data
                        level = data[2]
                        xp = data[3] + 20  # The amount of xp to give to the user
                        messages = data[4] + 1
                        xp_needed = 100 * (1.5 if level > 30 else 2) ** level  # Calculate the XP needed for the next level

                        if xp >= xp_needed:
                            # Level up the user if they have enough XP
                            level += 1
                            xp = 0
                            desc=f'You leveled up to {level}.\n'
                            # Check if the user reached a level with a role
                            if level in role_levels:
                                role_index = role_levels.index(level)
                                prev_role_index = role_index - 1 if role_index > 0 else None
                                
                                if prev_role_index is not None:
                                    prev_role_name = role_names[prev_role_index]
                                    prev_role = discord.utils.get(message.guild.roles, name=prev_role_name)
                                    await message.author.remove_roles(prev_role)

                                current_role_name = role_names[role_index]
                                role = discord.utils.get(message.guild.roles, name=current_role_name)
                                if role is None:
                                    # Create the role if it doesn't exist
                                    role = await message.guild.create_role(name=current_role_name)
                                await message.author.add_roles(role)
                                desc += f'You have been given the title **{current_role_name}**.'

                            msg = discord.Embed(title=f"{message.author.display_name} Congratulations!",
                                                    description=desc,
                                                    color=discord.Color.random())
                            level_up = await message.channel.send(embed=msg)
                            await asyncio.sleep(5)
                            await level_up.delete()

                        # Update the user's leveling data in the database
                        await cursor.execute('UPDATE leveling SET level = ?, xp = ?, messages = ? WHERE guild_id = ? AND user_id = ?', (level, xp, messages, message.guild.id, message.author.id))

                    await self.bot.db.commit()
    # Command to check the user's level and XP
    @commands.hybrid_command()
    async def profile(self, ctx, user:discord.Member=None):
        """Check a your a user's profile."""
        if user is None:
            user=ctx.author
        uid = int(user.id)
        user = ctx.guild.get_member(uid)
        
        # Get the user's leveling data
        cursor = await self.bot.db.cursor()
        await cursor.execute('SELECT * FROM leveling WHERE guild_id = ? AND user_id = ?', (ctx.guild.id, user.id))
        data = await cursor.fetchone()

        if data is None:
            await ctx.send("You haven't sent any messages in this server yet.")
        else:
            level = data[2]
            xp = data[3]
            xp_needed = 100 * (1.5 if level > 30 else 2) ** level  # Calculate the XP needed for the next level
            xp_remaining = xp_needed - xp
            msg_count = data[4]

            if msg_count >= 10:
                msg_count = f'{msg_count/10 :.2f}k'

            # Get leaderboard data
            await cursor.execute('SELECT user_id, level, xp FROM leveling WHERE guild_id = ? ORDER BY level DESC, xp DESC', (ctx.guild.id,))
            leaderboard_data = await cursor.fetchall()

            # Calculate the user's rank
            user_rank = next((i + 1 for i, row in enumerate(leaderboard_data) if row[0] == user.id), None)

            # Get the user's roles
            roles = user.roles

            # Find the common roles between the user's roles and the desired roles
            common_roles = [role.mention for role in roles if role.name in role_names]

            # Calculate the progress towards the next level
            xp_percent = (xp / xp_needed) * 100
            progress_bar = f"{'██' * int(xp_percent / 10)}{'--' * (10 - int(xp_percent / 10))} {xp_percent:.2f}%"

            # Checking User online presence
            status = user.status

            if 'online' in status:
                status = '<:1514onlineblank:1159758971087888404>'

            elif 'dnd' in status:
                status = '<:4431dndblank:1159758965463322706>'
            
            elif 'idle' in status:
                status = '<:5204idleblank:1159758961948512306>'

            elif 'offline' in status:
                status = '<:6610invisibleofflineblank:1159758967564668929>'
            

            #Checking if the user is a server booster or not
            if user in ctx.guild.premium_subscribers:
                boost= 'Yes'
            else:
                boost = 'No'

            #description part of embed
            desc = f"**LEVEL INFO\nUsername :** {user.name}\n"

            if user_rank is not None:
                if user_rank == 1:
                    user_rank='🥇'
                elif user_rank == 2:
                    user_rank='🥈'
                elif user_rank == 3:
                    user_rank='🥉'
                else:
                    user_rank=f'#{user_rank}'

                desc += f"**Ranking:** {user_rank}\n"

            if common_roles:
                desc += f"**Rank:** {common_roles[0]}\n"

            desc += f'**Level:** {level}\n**XP:** {xp}/{xp_needed}\n**No. of Messages Sent:** {msg_count}\n'
            desc += f'**Progress to Next Level :\n{progress_bar}**\n**XP till next level:** {xp_remaining}\n\n'

            desc += f'**ACCOUNT INFO\nStatus : {status}\nServer Booster : {boost}**\n'
            desc += f'**Joined at :** {discord.utils.format_dt(user.joined_at,style="R")} / {discord.utils.format_dt(user.joined_at,style="f")}\n'
            desc += f'**Created at :** {discord.utils.format_dt(user.created_at,style="R")} / {discord.utils.format_dt(user.created_at,style="f")}\n'
            desc += f'**Active Roles : ** {", ".join([role.mention for role in user.roles])}'
            
            # Create an embed to display the level information and rank
            embed = discord.Embed(title=f"{user.display_name}'s Profile",
                                  color=discord.Color.random(),
                                  description=desc)
            embed.set_thumbnail(url=user.display_avatar.url)

            await ctx.send(embed=embed)

    @commands.hybrid_command()
    @commands.has_role(admin)
    async def delete_data(self, ctx,user:discord.Member=None):
        """Delete a users data."""
        if user is None:
            user=ctx.author
        async with aiosqlite.connect("leveling.db") as conn:
            await conn.execute(
                "DELETE FROM leveling WHERE guild_id = ? AND user_id = ?",
                (ctx.guild.id, user.id),
            )
            await conn.commit()
        
        await ctx.send(f"{user.display_name}'s data has been deleted.")



    @commands.hybrid_command()
    async def leaderboard(self, ctx):
        """Check the guild's top 5 rankers."""
        cursor = await self.bot.db.cursor()
        await cursor.execute('SELECT user_id, level, xp FROM leveling WHERE guild_id = ? ORDER BY level DESC, xp DESC', (ctx.guild.id,))
        leaderboard_data = await cursor.fetchall()

        if leaderboard_data:
            embed = discord.Embed(title=f"{ctx.guild.name}'s Leaderboard", color=discord.Color.gold())

            # Limit the leaderboard_data to the top 5 users
            top_5_data = leaderboard_data[:5]

            for index, data in enumerate(top_5_data, start=1):
                member_id, level, xp = data
                member = ctx.guild.get_member(member_id)
                if member is not None:
                    embed.add_field(name=f"{index}. {member.display_name}", value=f"**Level: {level} | XP:** {xp}", inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No leaderboard data available.")

        await cursor.close()
