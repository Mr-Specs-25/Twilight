import discord
from discord import app_commands
from discord.ext import commands, tasks

class User(commands.Cog):
    def __init__(self, client: commands.Client) -> None:
        self.client = client

@app_commands.guild_only()
class Group(app_commands.Group):

    @app_commands.command(name="cog", description="cog test")
    async def cog(self, interaction:discord.Interaction) -> None:
        await interaction.response.send_message("hello!", ephemeral=True)

async def setup(client: commands.Client) -> None:
    await client.add_cog(User(client))