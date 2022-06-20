import discord

from discord.ext import commands


class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client


#load-extension
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        await ctx.message.delete()
        self.client.load_extension(f"cogs.{extension}")
        channel = self.client.get_channel(988487504812441610)
        embed = discord.Embed(color = 0xf9ffff, description = f"```py\n Successfully loaded {extension}```", timestamp = ctx.message.created_at)
        embed.set_author(name = "Extension loaded", icon_url = self.client.user.avatar_url)
        await ctx.send(f"```py\n Successfully loaded {extension}```", delete_after = 5.0)
        await channel.send(embed = embed)

#unload-extension
    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        await ctx.message.delete()
        self.client.unload_extension(f"cogs.{extension}")
        channel = self.client.get_channel(988487504812441610)
        embed = discord.Embed(color = 0xf9ffff, description = f"```py\n Successfully unloaded {extension}```", timestamp = ctx.message.created_at)
        embed.set_author(name = "Extension unloaded", icon_url = self.client.user.avatar_url)
        await ctx.send(f"```py\n Successfully unloaded {extension}```", delete_after = 5.0)
        await channel.send(embed = embed)

#reload_extension
    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension):
        await ctx.message.delete()
        self.client.unload_extension(f"cogs.{extension}")
        self.client.load_extension(f"cogs.{extension}")
        channel = self.client.get_channel(988487504812441610)
        embed = discord.Embed(color = 0xf9ffff, description = f"```py\n Successfully reloaded {extension}```", timestamp = ctx.message.created_at)
        embed.set_author(name = "Extension reloaded", icon_url = self.client.user.avatar_url)
        await ctx.send(f"```py\n Successfully reloaded {extension}```", delete_after = 5.0)
        await channel.send(embed = embed)


#clear-dms
    @commands.command()
    @commands.is_owner()
    async def cleardms(self, ctx, limit: int = None):
        await ctx.message.delete()
        passed = 0
        failed = 0
        async for message in ctx.message.channel.history(limit = limit):
            if message.author.id == self.client.user.id:
                try:
                    await message.delete()
                    passed += 1
                except:
                    failed += 1
        channel = self.client.get_channel(988487504812441610)
        embed = discord.Embed(color = 0xf9ffff, description = f"```py\n Removed {passed} messages with {failed} fails```", timestamp = ctx.message.created_at)
        embed.set_author(name = "DMs cleared", icon_url = self.client.user.avatar_url)
        await ctx.send(f"```py\n Removed {passed} messages with {failed} fails```", delete_after = 5.0)
        await channel.send(embed = embed)


#massping
    @commands.command()
    @commands.is_owner()
    async def massping(ctx, times : int, member: discord.Member = None):
        await ctx.message.delete()
        if times <= 100:
            for i in range(times):
                await ctx.send(member.mention)


def setup(client):
    client.add_cog(Owner(client))