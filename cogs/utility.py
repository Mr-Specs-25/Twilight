import discord
import random

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

#fake-nuke
    @commands.command()
    async def nuke(self, ctx):
        await ctx.message.delete()
        if isinstance(ctx.message.channel, discord.TextChannel):
            initial = random.randrange(15, 25)
            message = await ctx.send(f"```diff\n- Nuking {ctx.guild.name}..., will take {initial} seconds to complete```")
            await sleep(2)
            await message.edit(
                content = f"```diff\n- Nuking {ctx.guild.name}..., will take {initial} seconds to complete \n\nDeleting {len(ctx.guild.roles)} Roles...```")
            await sleep(2)
            await message.edit(
                content = f"```diff\n- Nuking {ctx.guild.name}..., will take {initial} seconds to complete \n\nDeleting {len(ctx.guild.roles)} Roles... \n\nDeleting {len(ctx.guild.text_channels)} Text Channels...```")
            await sleep(2)
            await message.edit(
                content = f"```diff\n- Nuking {ctx.guild.name}..., will take {initial} seconds to complete \n\nDeleting {len(ctx.guild.roles)} Roles... \n\nDeleting {len(ctx.guild.text_channels)} Text Channels... \n\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...```")
            await sleep(2)
            await message.edit(
                content = f"```diff\n- Nuking {ctx.guild.name}..., will take {initial} seconds to complete \n\nDeleting {len(ctx.guild.roles)} Roles... \n\nDeleting {len(ctx.guild.text_channels)} Text Channels... \n\nDeleting {len(ctx.guild.voice_channels)} Voice Channels... \n\nDeleting {len(ctx.guild.categories)} Categories...```")
            await sleep(2)
            await message.edit(
                content = f"```diff\n- Nuking {ctx.guild.name}..., will take {initial} seconds to complete \n\nDeleting {len(ctx.guild.roles)} Roles... \n\nDeleting {len(ctx.guild.text_channels)} Text Channels... \n\nDeleting {len(ctx.guild.voice_channels)} Voice Channels... \n\nDeleting {len(ctx.guild.categories)} Categories... \n\nDeleting Webhooks...```")
            await sleep(2)
            await message.edit(
                content = f"```diff\n- Nuking {ctx.guild.name}..., will take {initial} seconds to complete \n\nDeleting {len(ctx.guild.roles)} Roles... \n\nDeleting {len(ctx.guild.text_channels)} Text Channels... \n\nDeleting {len(ctx.guild.voice_channels)} Voice Channels... \n\nDeleting {len(ctx.guild.categories)} Categories... \n\nDeleting Webhooks... \n\nDeleting Emojis```")
            await sleep(2)
            await message.edit(
                content = f"```diff\n- Nuking {ctx.guild.name}..., will take {initial} seconds to complete \n\nDeleting {len(ctx.guild.roles)} Roles... \n\nDeleting {len(ctx.guild.text_channels)} Text Channels... \n\nDeleting {len(ctx.guild.voice_channels)} Voice Channels... \n\nDeleting {len(ctx.guild.categories)} Categories... \n\nDeleting Webhooks... \n\nDeleting Emojis \n\nInitiating Ban Wave...```")
            await sleep(2)
            await message.edit(
                content = f"```diff\n- Nuking {ctx.guild.name}..., will take {initial} seconds to complete \n\nDeleting {len(ctx.guild.roles)} Roles... \n\nDeleting {len(ctx.guild.text_channels)} Text Channels... \n\nDeleting {len(ctx.guild.voice_channels)} Voice Channels... \n\nDeleting {len(ctx.guild.categories)} Categories... \n\nDeleting Webhooks... \n\nDeleting Emojis \n\nInitiating Ban Wave... \n\nInitiating Mass-DM```")
            await sleep(2)
            await message.edit(
                content = f"```diff\n-- -- -- -- -- --Operation Successful!-- -- -- -- -- --``` \nhttps://tenor.com/view/boom-explosion-gif-12797649")


def setup(client):
    client.add_cog(Utility(client))

