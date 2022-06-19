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

#transformer
    @commands.command()
    async def _1337_speak(self, ctx, *, text=None):
        await ctx.message.delete()
        text = text.replace("a", "4").replace("A", "4").replace("e", "3").replace("E", "3") \
            .replace("i", "!").replace("I", "!").replace("o", "0").replace("O", "0") \
            .replace("u", "|_|").replace("U", "|_|").replace("k", "|<").replace("K", "|<") \
            .replace("l", "|").replace("L", "|_").replace("b", "6").replace("B", "8") \
            .replace("h", "|-,").replace("H", "|-|").replace("v", "\\/").replace("\\/")
        await ctx.send(f"{text}")

#fake-nuke
    @commands.command()
    async def nuke(self, ctx):
        await ctx.message.delete()
        if isinstance(ctx.message.channel, discord.TextChannel):
            print("hi")
            initial = random.randrange(5,15)
            message = await ctx.send(f"```diff\n- Nuking {ctx.guild.name}..., will take {initial} seconds to complete```\n")
            await sleep(1)
            await message.edit(
                content = f"```yaml\n- Nuking {ctx.guild.name}..., will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\n```")
            await sleep(1)
            await message.edit(
                content = f"```diff\n- Nuking {ctx.guild.name}..., will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...```")
            await sleep(1)
            await message.edit(
                content = f"```yaml\n- Nuking {ctx.guild.name}..., will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...```")
            await sleep(1)
            await message.edit(
                content = f"```diff\n- Nuking {ctx.guild.name}..., will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...```")
            await sleep(1)
            await message.edit(
                content = f"```yaml\n- Nuking {ctx.guild.name}..., will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...```")
            await sleep(1)
            await message.edit(
                content = f"```diff\n- Nuking {ctx.guild.name}..., will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis```")
            await sleep(1)
            await message.edit(
                content = f"```yaml\n- Nuking {ctx.guild.name}..., will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...```")
            await sleep(1)
            await message.edit(
                content = f"```diff\n- Nuking {ctx.guild.name}..., will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...\nInitiating Mass-DM```")
            await sleep(1)
            await message.edit(
                content = f"```diff\n-- -- -- -- -- --Operation Successful!-- -- -- -- -- --")

def setup(client):
    client.add_cog(Utility(client))

