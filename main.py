import discord
import os

from discord.ext import commands

from datetime import datetime
from time import time


#setup
client = discord.Client()
intents = discord.Intents.all()
intents.members = True
intents.presences = True

TOKEN = os.getenv("TOKEN")

client = commands.Bot(command_prefix = "--", intents = intents)
client.remove_command("help")
client.launch_time = datetime.utcnow()


X_Mark = ("<:T_XMark:871079164554387541>")


#status
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game(name = f"--help┃Roaming around Twilight Hangout!"))
    print ("Radon\'s Ready!")

#error-handling
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      missing_perms_embed = discord.Embed(title = f"{X_Mark} Missing Permissions", description = f"You need **{', '.join(error.missing_perms)}** Permission to run this Command", color =  ctx.author.color, timestamp = ctx.message.created_at)
      missing_perms_embed.set_footer(text = f"Missing Permission!")
      await ctx.send(embed = missing_perms_embed, delete_after = 10.0)
    if isinstance(error, commands.MissingRequiredArgument):
      missing_args_embed = discord.Embed(title = f"{X_Mark} Missing Agrument", description = f"Your missing **{error.param}** to run this Command", color =  ctx.author.color, timestamp = ctx.message.created_at)
      missing_args_embed.set_footer(text = f"Bad Argument!")
      await ctx.send(embed = missing_args_embed, delete_after = 10.0)
    if isinstance(error, commands.CommandOnCooldown):
      cooldown_embed = discord.Embed(title = f"{X_Mark} Command on Cooldown", description = f"You will be able to run this Command after `{round(error.retry_after)} seconds` ", color = ctx.author.color, timestamp = ctx.message.created_at)
      cooldown_embed.set_footer(text = f"Cooldown!")
      await ctx.send(embed = cooldown_embed, delete_after = 10.0)


#basic
@client.command()
async def ping(ctx):
    start = time()
    message = await ctx.send(f"```Pong! \nLATENCY: {client.latency*1000:,.0f} ms```")
    end = time()
    await message.edit(content=f"```Pong! \nLATENCY: {client.latency*1000:,.0f} ms \nRESPONSE TIME: {(end-start)*1000:,.0f} ms```")

@client.command()
@commands.is_owner()
async def massping(ctx, times : int, member: discord.Member = None):
    await ctx.message.delete()
    if times <= 100:
        for i in range(times):
            await ctx.send(member.mention)




#load-extensions
client.load_extension("cogs.information")
client.load_extension("cogs.moderation")
client.load_extension("cogs.utility")
client.load_extension("cogs.events")
client.load_extension("cogs.eval")


client.run(TOKEN)


