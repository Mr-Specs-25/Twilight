import discord
import typing

from discord.ext import commands
from discord import User, errors
from discord.ext.commands import has_permissions
from discord.ext.commands.errors import MissingPermissions

#========================================================================================================================
#========================================================================================================================

#emotes
Info       = ("<:RA_Stats:871077269387509831>")
Utility    = ("<:RA_Utility:871077840349720607>")
Moderation = ("<:RA_BanHammer:871077232020439090>")
Games      = ("<:RA_Games:871077302270820424>")
Bullet     = ("<:RA_Bullet:871077168791294012>")
X_Mark     = ("<:RA_XMark:871079164554387541>")

#========================================================================================================================
#========================================================================================================================

class Mdoeration(commands.Cog):
    def __init__(self, client):
        self.client = client

#========================================================================================================================
#========================================================================================================================


    @commands.group(name = 'swipe', hidden = True, invoke_without_command = True, aliases = ["purge"])
    @commands.has_permissions(manage_messages = True)
    async def swipe(self, ctx, num_messages: int):
        """Clear <n> messages from current channel"""
        channel = ctx.message.channel
        await ctx.message.delete()
        if num_messages <= 0:
          em = discord.Emebed(title = "Bad Argument!", description = "usage = -swipe <+ve int>", color = ctx.author.color)
          await ctx.reply(embed = em)
        else:
          await channel.purge(limit = num_messages, check = None, before = None)
          await ctx.send(f'> **{num_messages}** Messages Swiped, Yummy..... Tastes good!', delete_after = 5.0)
          return True


    @swipe.group(name = 'until', hidden = True)
    @commands.has_permissions(manage_messages = True)
    async def until(self, ctx, message_id: int,):
        """Clear messages in a channel until the given message_id. Given ID is not deleted"""
        channel = ctx.message.channel
        await ctx.message.delete()
        try:
            message = await channel.fetch_message(message_id)
        except errors.NotFound:
            em = discord.Embed(title = "Message NotFound!", description = "usage: -swipe until <msg_id>")
            await ctx.reply(embed = em, delete_after = 5.0)
            return
        await channel.purge(after = message)
        await ctx.send('> Messages Swiped, Yummy..... Tastes good!', delete_after = 5.0)
        return True


    @swipe.group(name = 'user', hidden = True)
    @commands.has_permissions(manage_messages = True)
    async def user(self, ctx, user: User, num_messages: typing.Optional[int] = 150):
        """Clear all messagges of <User> withing the last [n = 200] messages"""
        channel = ctx.message.channel
        await ctx.message.delete()
        def check(msg):
            return msg.author.id == user.id
        if num_messages <= 0:
          em = discord.Emebed(title = "Bad Argument!", description = "usage = -swipe <user> <+ve int>", color = ctx.author.color)
          await ctx.reply(embed = em)
        else:
          await channel.purge(limit = num_messages, check = check, before = None)
          await ctx.send(f'> **{num_messages}** Messages Swiped, Yummy..... Tastes good!', delete_after = 5.0)


#========================================================================================================================
#========================================================================================================================
#ErrorHandling....

    @swipe.error
    async def swipe_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
          bad_arg_embed = discord.Embed(title = f"Bad Argument!", description = "usage: -swipe <+ve int>", color = ctx.author.color)
          await ctx.reply(embed = bad_arg_embed)

    @until.error
    async def until_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
          bad_arg_embed = discord.Embed(title = f"Bad Argument!", description = "usage: -swipe until <msg_id>", color = ctx.author.color)
          await ctx.reply(embed = bad_arg_embed)

    @user.error
    async def user_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
          bad_arg_embed = discord.Embed(title = f"Bad Argument!", description = "usage: -swipe user <user> [+ve int]", color = ctx.author.color)
          await ctx.send(embed = bad_arg_embed)
        if isinstance(error, commands.MissingRequiredArgument):
          bad_arg_embed = discord.Embed(title = f"Missing Argument!", description = "usage: -swipe user <user> [+ve int]", color = ctx.author.color)
          await ctx.send(embed = bad_arg_embed)

#========================================================================================================================
#========================================================================================================================

def setup(client):
    client.add_cog(Mdoeration(client))

#========================================================================================================================
#========================================================================================================================
