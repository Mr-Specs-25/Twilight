import discord

from discord.ext import commands
from asyncio import sleep


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

#massping
    @commands.command()
    @commands.is_owner()
    async def massping(ctx, times : int, member: discord.Member = None):
        await ctx.message.delete()
        if times <= 100:
            for i in range(times):
                await ctx.send(member.mention)


def setup(client):
    client.add_cog(Utility(client))

