import discord

from discord.ext import commands
from asyncio import sleep


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client


#todo--


def setup(client):
    client.add_cog(Utility(client))

