import discord

from discord.ext import commands
from asyncio import sleep


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    X_Mark = ("<:T_XMark:871079164554387541>")


#error-handling
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            missing_perms_embed = discord.Embed(title = f"{self.X_Mark} **Missing Permissions!**", description = f"You need `{', '.join(error.missing_perms)}` permission to run this command", color = ctx.author.color, timestamp = ctx.message.created_at)
            await ctx.send(embed = missing_perms_embed, delete_after = 10.0)
        if isinstance(error, commands.MissingRequiredArgument):
            missing_args_embed = discord.Embed(title = f"{self.X_Mark} **Missing Agrument!**", description = f"You're missing `{error.param}` to run this command", color =  ctx.author.color, timestamp = ctx.message.created_at)
            await ctx.send(embed = missing_args_embed, delete_after = 10.0)
        if isinstance(error, commands.CommandOnCooldown):
            cooldown_embed = discord.Embed(title = f"{self.X_Mark} **Command on Cooldown!**", description = f"You'll be able to run this command after `{round(error.retry_after)} seconds`", color = ctx.author.color, timestamp = ctx.message.created_at)
            await ctx.send(embed = cooldown_embed, delete_after = 10.0)


#statistics
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await sleep(60*5)
        for channel in member.guild.channels:
            if channel.name.startswith("🎯〢Members:"):
                await channel.edit(name = f"🎯〢Members: {member.guild.member_count}")
                break

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await sleep(60*5)
        for channel in member.guild.channels:
            if channel.name.startswith("🎯〢Members:"):
                await channel.edit(name = f"🎯〢Members: {member.guild.member_count}")
                break


#logging
    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload):
      message = payload.cached_message
      if(message.guild):
        if message.guild.name == "Twilight Hangout":
          delem = discord.Embed(color = message.author.colour)
          delem.set_author(name = message.author, icon_url = message.author.avatar_url)
          delem.add_field(name = f"**Message deleted** \nChannel: #{message.channel.name}", value = f"\n**Content:** \n\t{message.content}")
          delem.set_footer(text = f"{message.guild} | {message.guild.id}")
          channel = self.client.get_channel(839431570401918987)
          await channel.send(embed = delem)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
      if(after.guild):
        if after.guild.name == "Twilight Hangout":
          if before.content != after.content:
            edem = discord.Embed(color = after.author.colour)
            edem.set_author(name = after.author, icon_url = after.author.avatar_url)
            edem.add_field(name = f"**Message edited** \nChannel: #{after.channel.name}", value = f"\n**Before:** {before.content} \n**+After:** {after.content}")
            edem.set_footer(text = f"{after.guild} | {after.guild.id}")
            channel = self.client.get_channel(839431570401918987)
            await channel.send(embed = edem)


def setup(client):
    client.add_cog(Events(client))

