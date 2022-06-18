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


#status
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game(name = f"--help┃Roaming around Twilight Hangout!"))
    print ("Radon\'s Ready!")

#basic
@client.command()
async def ping(ctx):
    start = time()
    message = await ctx.send(f"```Pong! \nLATENCY: {client.latency*1000:,.0f} ms```")
    end = time()
    await message.edit(content=f"```Pong! \nLATENCY: {client.latency*1000:,.0f} ms \nRESPONSE TIME: {(end-start)*1000:,.0f} ms```")





#load-extensions
for filename in os.listdir("./cogs"):
      if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")

client.run(TOKEN)


