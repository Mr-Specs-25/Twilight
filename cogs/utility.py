import discord
import requests
import urllib.parse

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

#ascii
    @commands.command()
    async def ascii(self, ctx, *, text=None):
        await ctx.message.delete()
        r = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}").text
        if len('```' + r + '```') > 2000:
            return
        await ctx.send(f"```{r}```")


def setup(client):
    client.add_cog(Utility(client))

