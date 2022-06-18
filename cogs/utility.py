import discord

from discord.ext import commands
from asyncio import sleep

#========================================================================================================================
#========================================================================================================================

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

#========================================================================================================================
#========================================================================================================================

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await sleep(60*5)
        for channel in member.guild.channels:
            if channel.name.startswith("〢🎯Members:"):
                await channel.edit(name = f"〢🎯Members: {member.guild.member_count}")
                break

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await sleep(60*5)
        for channel in member.guild.channels:
            if channel.name.startswith("〢🎯Members:"):
                await channel.edit(name = f"〢🎯Members: {member.guild.member_count}")
                break

#========================================================================================================================
#========================================================================================================================

def setup(client):
    client.add_cog(Utility(client))

#========================================================================================================================
#========================================================================================================================