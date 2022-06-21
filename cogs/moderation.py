import discord
import typing

from discord.ext import commands
from discord import User, errors
from discord.ext.commands import has_permissions
from discord.ext.commands.errors import MissingPermissions


class Mdoeration(commands.Cog):
    def __init__(self, client):
        self.client = client

#swipe
    @commands.group(name = "swipe", hidden = True, invoke_without_command = True, aliases = ["purge"])
    @commands.has_permissions(manage_messages = True)
    async def swipe(self, ctx, num_messages: int):
        channel = ctx.message.channel
        await ctx.message.delete()
        if num_messages <= 0:
          em = discord.Emebed(title = "Bad Argument!", description = "usage = -swipe <+ve int>", color = ctx.author.color)
          await ctx.reply(embed = em)
        else:
          await channel.purge(limit = num_messages, check = None, before = None)
          await ctx.send(f"***Successfully purged! `[{num_messages}]`***", delete_after = 5.0)
          return True

#swipe-until
    @swipe.group(name = "until", hidden = True)
    @commands.has_permissions(manage_messages = True)
    async def until(self, ctx, message_id: int,):
        channel = ctx.message.channel
        await ctx.message.delete()
        try:
            message = await channel.fetch_message(message_id)
        except errors.NotFound:
            em = discord.Embed(title = "Message NotFound!", description = "usage: -swipe until <msg_id>")
            await ctx.reply(embed = em, delete_after = 5.0)
            return
        await channel.purge(after = message)
        await ctx.send("***Successfully purged!***", delete_after = 5.0)
        return True

#swipe-user
    @swipe.group(name = "user", hidden = True)
    @commands.has_permissions(manage_messages = True)
    async def user(self, ctx, user: User, num_messages: typing.Optional[int] = 150):
        channel = ctx.message.channel
        await ctx.message.delete()
        def check(msg):
            return msg.author.id == user.id
        if num_messages <= 0:
          em = discord.Emebed(title = "Bad Argument!", description = "usage = -swipe <user> <+ve int>", color = ctx.author.color)
          await ctx.reply(embed = em)
        else:
          await channel.purge(limit = num_messages, check = check, before = None)
          await ctx.send(f"***Successfully purged! `[{num_messages}]`***", delete_after = 5.0)


def setup(client):
    client.add_cog(Mdoeration(client))


