import discord
import random

from discord.ext import commands
from asyncio import sleep

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client


#fake-nuke
    @commands.command()
    @commands.has_role(987597496857546792)
    async def nuke(self, ctx):
        await ctx.message.delete()
        if isinstance(ctx.message.channel, discord.TextChannel):
            initial = random.randrange(15, 25)
            message = await ctx.send(f"```diff\n-- Nuking {ctx.guild.name}, will take {initial} seconds to complete...```")
            await sleep(2)
            await message.edit(
                content = f"```diff\n-- Nuking {ctx.guild.name}, will take {initial} seconds to complete... \n\t\tDeleting {len(ctx.guild.roles)} Roles...```")
            await sleep(2)
            await message.edit(
                content = f"```diff\n-- Nuking {ctx.guild.name}, will take {initial} seconds to complete... \n\t\tDeleting {len(ctx.guild.roles)} Roles... \n\t\tDeleting {len(ctx.guild.text_channels)} Text Channels...```")
            await sleep(2)
            await message.edit(
                content = f"```diff\n-- Nuking {ctx.guild.name}, will take {initial} seconds to complete... \n\t\tDeleting {len(ctx.guild.roles)} Roles... \n\t\tDeleting {len(ctx.guild.text_channels)} Text Channels... \n\t\tDeleting {len(ctx.guild.voice_channels)} Voice Channels...```")
            await sleep(2)
            await message.edit(
                content = f"```diff\n-- Nuking {ctx.guild.name}, will take {initial} seconds to complete... \n\t\tDeleting {len(ctx.guild.roles)} Roles... \n\t\tDeleting {len(ctx.guild.text_channels)} Text Channels... \n\t\tDeleting {len(ctx.guild.voice_channels)} Voice Channels... \n\t\tDeleting {len(ctx.guild.categories)} Categories...```")
            await sleep(2)
            await message.edit(
                content = f"```diff\n-- Nuking {ctx.guild.name}, will take {initial} seconds to complete... \n\t\tDeleting {len(ctx.guild.roles)} Roles... \n\t\tDeleting {len(ctx.guild.text_channels)} Text Channels... \n\t\tDeleting {len(ctx.guild.voice_channels)} Voice Channels... \n\t\tDeleting {len(ctx.guild.categories)} Categories... \n\t\tDeleting Webhooks...```")
            await sleep(2)
            await message.edit(
                content = f"```diff\n-- Nuking {ctx.guild.name}, will take {initial} seconds to complete... \n\t\tDeleting {len(ctx.guild.roles)} Roles... \n\t\tDeleting {len(ctx.guild.text_channels)} Text Channels... \n\t\tDeleting {len(ctx.guild.voice_channels)} Voice Channels... \n\t\tDeleting {len(ctx.guild.categories)} Categories... \n\t\tDeleting Webhooks... \n\t\tDeleting Emojis```")
            await sleep(2)
            await message.edit(
                content = f"```diff\n-- Nuking {ctx.guild.name}, will take {initial} seconds to complete... \n\t\tDeleting {len(ctx.guild.roles)} Roles... \n\t\tDeleting {len(ctx.guild.text_channels)} Text Channels... \n\t\tDeleting {len(ctx.guild.voice_channels)} Voice Channels... \n\t\tDeleting {len(ctx.guild.categories)} Categories... \n\t\tDeleting Webhooks... \n\t\tDeleting Emojis \n\t\tInitiating Ban Wave...```")
            await sleep(2)
            await message.edit(
                content = f"```diff\n-- Nuking {ctx.guild.name}, will take {initial} seconds to complete... \n\t\tDeleting {len(ctx.guild.roles)} Roles... \n\t\tDeleting {len(ctx.guild.text_channels)} Text Channels... \n\t\tDeleting {len(ctx.guild.voice_channels)} Voice Channels... \n\t\tDeleting {len(ctx.guild.categories)} Categories... \n\t\tDeleting Webhooks... \n\t\tDeleting Emojis \n\t\tInitiating Ban Wave... \n\t\tInitiating Mass-DM```")
            await sleep(2)
            await message.edit(
                content = f"```diff\n-- -- -- -- -- --Operation Successful!-- -- -- -- -- --``` \nhttps://tenor.com/view/boom-explosion-gif-12797649")


def setup(client):
    client.add_cog(Utility(client))

