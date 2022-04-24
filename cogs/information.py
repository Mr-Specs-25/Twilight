import discord
import requests

from time import time
import datetime, time
from discord.ext import commands
from platform import python_version
from discord import __version__ as discord_version
from psutil import Process, virtual_memory
from discord.ext.commands.cooldowns import BucketType

#========================================================================================================================
#========================================================================================================================

class Information(commands.Cog):
    def __init__(self, client):
        self.client = client

#========================================================================================================================
#========================================================================================================================

    blue = discord.Color.from_rgb(50, 180, 250)
    green = discord.Color.from_rgb(50, 250, 180)
    red = discord.Color.from_rgb(250, 50, 50)

    Info       = ("<:RA_Stats:871077269387509831>")
    Utility    = ("<:RA_Utility:871077840349720607>")
    Moderation = ("<:RA_BanHammer:871077232020439090>")
    Games      = ("<:RA_Games:871077302270820424>")
    Bullet     = ("<:RA_Bullet:871077168791294012>")
    X_Mark     = ("<:RA_XMark:871079164554387541>")

    Online    =  ("<:RA_Online:871075685643452466>")
    DND       =  ("<:RA_DoNotDisturb:871075724906332221>")
    Idle      =  ("<:RA_Idle:871075755495395338>")
    Offline   =  ("<:RA_Offline:871075785883140166>")

    Info_cmds = ("user, server, check")
    Utility_cmds = ("")
    Moderation_cmds = ("swipe")
    Fun_cmds = ("")


#========================================================================================================================
#========================================================================================================================

    @commands.group(invoke_without_command = True, aliases = ["commands"], case_insensitive = True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def help(self, ctx):
        hembed = discord.Embed(title = "", description = "**Hi, I\'m your All time Companion!** ```yaml\nSubCommands: swipe/purge```", color = 0x00ffef, timestamp = ctx.message.created_at)
        hembed.set_author(name = "RADON COMMANDS", icon_url = self.client.user.avatar_url)
        hembed.set_thumbnail(url = self.client.user.avatar_url)
        hembed.add_field(name = f"{self.Info} Information", value = f"```{self.Info_cmds}```", inline = True)
        hembed.add_field(name = f"{self.Utility} Utility", value = f"```{self.Utility_cmds}```", inline = False)
        hembed.add_field(name = f"{self.Moderation} Moderation", value = f"```{self.Moderation_cmds}```", inline = False)
        hembed.add_field(name = f"{self.Games} Fun", value = f"```{self.Fun_cmds}```", inline = False)
        hembed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.reply(embed = hembed)

    @help.command(aliases = ["purge"])
    @commands.guild_only()
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def swipe(self, ctx):
      shem = discord.Embed(title = "", description = "```Aliase: purge \nSwipe Commands: swipe, swipe until, swipe user \n\nUsage: \n\tswipe: swipe <num_msgs> \n\tswipe until: swipe until <msg_id> \n\tswipe user: <user> <num_msgs>```", color = ctx.author.color, timestamp = ctx.message.created_at)
      shem.set_author(name = "Swipe Commands", icon_url = self.client.user.avatar_url)
      shem.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
      await ctx.reply(embed = shem)

#========================================================================================================================
#========================================================================================================================

    @commands.Cog.listener()
    async def on_ready(self):
        global startTime
        startTime = time.time()

    @commands.command()
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def info(self, ctx):
        RadonVersion = ("1.2.0")
        Uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
#        MemberCount = (len([m for m in ctx.guild.members if not m.bot]))
#        BotCount = (len([m for m in ctx.guild.members if m.bot]))
        embed = discord.Embed(title = "**Information**", description = f"```Ping: \n\tping: {self.client.latency*1000:,.0f}ms \n\tuptime: {Uptime} \nVersion: \n\tbot: {RadonVersion} \n\tdiscord.py: {discord_version}```",color = ctx.author.color, timestamp = ctx.message.created_at)
        embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

#========================================================================================================================
#========================================================================================================================

    @commands.group(invoke_without_command = True, aliases = ["account"], case_insensitive = True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def user(self, ctx, member : discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]
        uiembed = discord.Embed(tile = "", description = "```yaml\nSubCommands: avatar```", color = ctx.author.color, timestamp = ctx.message.created_at)
        uiembed.set_author(name = "User Information", url = "", icon_url = self.client.user.avatar_url)
        uiembed.set_thumbnail(url = member.avatar_url)
        uiembed.add_field(name = f"{self.Bullet} General Info:", value = f"```User Name: {member.name} \nUser Nikname: {member.nick} \nUser ID: {member.id}```", inline = True)
        uiembed.add_field(name = f"{self.Bullet} Account Creation:", value = member.created_at.strftime("```%a, %#d %B %Y, %I:%M %p (Coordinated Universal Time)```"), inline = False)
        uiembed.add_field(name = f"{self.Bullet} Joined at:", value = member.joined_at.strftime("```%a, %#d %B %Y, %I:%M %p (Coordinated Universal Time)```"), inline = False)
        uiembed.add_field(name = f"{self.Bullet} Highest Role:", value = member.top_role.mention, inline = False)
        uiembed.add_field(name = f"{self.Bullet} Roles [{len(roles)}]:", value = " ".join([role.mention for role in roles]), inline = False)
        uiembed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.reply(embed = uiembed)

    @user.command(aliases = ["av"])
    @commands.guild_only()
    @commands.cooldown(1, 8, commands.BucketType.user) 
    async def avatar(self, ctx, member : discord.Member = None):
        member = ctx.author if not member else member
        aembed = discord.Embed(title = ":frame_photo: Profile Picture", description = f'{member.mention} \n[Avatar URL]({ctx.author.avatar_url})', color = ctx.author.color, timestamp = ctx.message.created_at)
        aembed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        aembed.set_image(url = member.avatar_url)
        await ctx.reply(embed = aembed)

#========================================================================================================================
#========================================================================================================================

    @commands.group(invoke_without_command = True, aliases = ["guild"], case_insensitive = True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def server(self, ctx, guild: discord.Guild = None):
        #guild = ctx.message.guild
        #statuses = [len(list(filter(lambda m: str(m.status) == 'online', ctx.guild.members))),
                    #len(list(filter(lambda m: str(m.status) == 'idle', ctx.guild.members))),
                    #len(list(filter(lambda m: str(m.status) == 'dnd', ctx.guild.members))),
                    #len(list(filter(lambda m: str(m.status) == 'invisible', ctx.guild.members)))]
        sembed = discord.Embed(title = '', description = '```yaml\nSubCommands: icon```', color = ctx.author.color, timestamp = ctx.message.created_at)
        sembed.set_thumbnail(url = ctx.guild.icon_url)
        sembed.set_author(name = 'Server Information', url = '', icon_url = self.client.user.avatar_url)
        sembed.add_field(name = f'{self.Bullet} General Info:', value = f'```Server ID: {ctx.guild.id} \nServer Region: {ctx.guild.region} \nServer Owner: {ctx.guild.owner} [{ctx.guild.owner_id}] \nServer Roles: {len(ctx.guild.roles)} \nVerification Level: {ctx.guild.verification_level}```', inline = False)
        sembed.add_field(name = f'{self.Bullet} Channel Info:', value = f'```Total Caategories: {len(ctx.guild.categories)} \nTotal Channels: {len(ctx.guild.channels)} \nText Channels: {len(ctx.guild.text_channels)} \nVoice Channels: {len(ctx.guild.voice_channels)}```', inline = True)
        sembed.add_field(name = f'{self.Bullet} Member Info:', value = f'```Total Members: {ctx.guild.member_count} \nTotal Humans: {len(list(filter(lambda m: not m.bot, ctx.guild.members)))} \nTotal Bots: {len(list(filter(lambda m: m.bot, ctx.guild.members)))} \nBanned Members: {len(await ctx.guild.bans())}```', inline = True)
        sembed.add_field(name = f'{self.Bullet} Boost Info:', value = f'```Server Boosts: {ctx.guild.premium_subscription_count} \nServer Boost Tier: {ctx.guild.premium_tier} \nServer Booster Role: {ctx.guild.premium_subscriber_role}```', inline = False)
        sembed.add_field(name = f'{self.Bullet} Server Creation:', value = ctx.guild.created_at.strftime('```%a, %#d %B %Y, %I:%M %p (Coordinated Universal Time)```'), inline = False)
        sembed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.reply(embed = sembed)

    @server.command()
    @commands.guild_only()
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def icon(self, ctx):
        aembed = discord.Embed(title = ":frame_photo: Server Icon", description = f'**{ctx.guild}** \n[Server Icon URL]({ctx.guild.icon_url})', color = ctx.author.color, timestamp = ctx.message.created_at)
        aembed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        aembed.set_image(url = ctx.guild.icon_url)
        await ctx.reply(embed = aembed)

#========================================================================================================================
#========================================================================================================================


    @commands.group(invoke_without_command = True, aliases = ["inspect"], case_insensitive = True)
    async def check(self, ctx):
      chem = discord.Embed(title = "", description = "```SubCommands: invite, emote  \n\nUsage: \n\tinvite: check invite <invite_link> \n\temote: check emote <emote>```", color = ctx.author.color, timestamp = ctx.message.created_at)
      chem.set_author(name = f"Check Command", url = '', icon_url = self.client.user.avatar_url)
      chem.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
      await ctx.reply(embed = chem, delete_after = 10.0)


    @check.command()
    @commands.guild_only()
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def invite(self, ctx, invite: discord.Invite):
      Inviter = invite.inviter if invite.inviter else "Unknown"
      InviterID = invite.inviter.id
      InvChannelName = invite.channel.name
      InvChannelID = invite.channel.id
      InviteServer = invite.guild
      InviteServerID = invite.guild.id
      InvServerDesc = invite.guild.description or "No Description Set"
      InvTotalMembers = invite.approximate_member_count
      InvActiveMembers = invite.approximate_presence_count

      invem = discord.Embed(title = "", description = "", color = ctx.author.color, timestamp = ctx.message.created_at)
      invem.set_author(name = "Invite Information", url = "", icon_url = self.client.user.avatar_url)
      invem.add_field(name = f"{self.Bullet} General Info:", value = f"```Invite Creater: \n\tInviter: {Inviter} \n\tID: {InviterID} \nInvite Channel: \n\tName: #{InvChannelName} \n\tID: {InvChannelID} \nInvite Server: \n\tServer Name: {InviteServer} \n\tID: {InviteServerID} \n\tTotal Members: {InvTotalMembers} \n\tActive Members: {InvActiveMembers} \n\tServer Description: {InvServerDesc}```", inline = True)
      invem.set_footer(text = f'Requested by {ctx.author}', icon_url = ctx.author.avatar_url)
      await ctx.send(embed = invem)


    @check.command(aliases = ["emoji"])
    @commands.guild_only()
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def emote(self, ctx, emoji: discord.Emoji = None):
        try:
            emoji = await emoji.guild.fetch_emoji(emoji.id)
        except discord.NotFound:
            return await ctx.send("> **I couldn't find this emote in this guild.**")

        is_animated = "Yes" if emoji.animated else "No"
        is_animated2 = "a" if emoji.animated else ""
        creation_time = emoji.created_at.strftime("%I:%M %p %B %d, %Y")
        #is_managed = "Yes" if emoji.managed else "No"
        #can_use_emoji = ("Everyone" if not emoji.roles else " ".join(role.name for role in emoji.roles))
        EmoteName = emoji.name
        EmoteID = emoji.id
        EmoteString = f"<{is_animated2}:{emoji.name}:{emoji.id}>"
        EmoteAuthor = emoji.user
        EmoteCreation = creation_time
        EmoteAnimated = is_animated
        GuildName = emoji.guild.name
        GuildID = emoji.guild.id

        embed = discord.Embed(title = "", description = f"```General Info: \n\tEmote Name: {EmoteName} \n\tEmote ID: {EmoteID} \n\tEmote String: {EmoteString} \n\tEmote Author: {EmoteAuthor} \n\tTime Created: {EmoteCreation} \nOther: \n\tAnimated: {EmoteAnimated} \n\tGuild Name: {GuildName} \n\tGuild ID: {GuildID}```", colour = ctx.author.color, timestamp = ctx.message.created_at)
        embed.set_author(name = f"Emote Information", url = "", icon_url = self.client.user.avatar_url)
        embed.set_thumbnail(url=emoji.url)
        embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.reply(embed=embed)


#========================================================================================================================
#=========================================================================================================================
#Error Handling...

    @emote.error
    async def emote_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
          bad_arg_embed = discord.Embed(title = f"Bad Argument!", description = "```Emote must be in this Server \nusage: -emote <emote_name>```", color = ctx.author.color)
          await ctx.reply(embed = bad_arg_embed)

#========================================================================================================================
#========================================================================================================================

def setup(client):
    client.add_cog(Information(client))

#========================================================================================================================
#========================================================================================================================
