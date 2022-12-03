import discord
from discord import app_commands
from discord.ext import commands, tasks

class User(commands.Cog):
    def __init__(self, client):
        self.client=client

    @app_commands.command(name="userinfo", description="sends user-details")
    async def cog(self, interaction:discord.Interaction, user:discord.User=None):
        user=interaction.message.author if not user else user
        embed=discord.Embed(title="User Details", color = interaction.message.author.color, timestamp = interaction.message.created_at)
        embed.add_field(name="Account creation: ", value=user.created_at.strftime("```%a, %#d %B %Y, %I:%M %p```"), inline=True)
        embed.add_field(name="Joined at: ", value=user.joined_at.strftime("```%a, %#d %B %Y, %I:%M %p```"), inline=True)
        embed.set_footer(text = f"Requested by {interaction.message.author}", icon_url = interaction.message.author.avatar_url)
        await interaction.response.send_message(embed=embed, ephemeral=False)

async def setup(client):
    await client.add_cog(User(client))