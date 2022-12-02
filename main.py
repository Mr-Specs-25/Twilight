import discord
import os
from discord import app_commands
from discord.ext import commands, tasks
from itertools import cycle
from dotenv import load_dotenv

intents=discord.Intents.all()
client=commands.Bot(command_prefix=";", intents=intents)
load_dotenv()
TOKEN=os.getenv("TOKEN")

status=cycle(["Songs", ";help"])
@client.event
async def on_ready():
    change_status.start()
    print("--Twilight\'s online!--")
    try:
        sync=await client.tree.sync()
        print(f"--commands synced: {len(sync)}--")
    except Exception as e:
        print(e)

@tasks.loop(minutes=5)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{status}"))

@client.tree.command(name="ping", description="sends client latency")
async def ping(interaction:discord.Interaction):
    await interaction.response.send_message(f"```Pong! \nLATENCY: {client.latency*1000:,.0f} ms```", ephemeral=True)


client.run(TOKEN)
