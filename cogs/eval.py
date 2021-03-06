import discord
import io
import textwrap
import traceback

from discord.ext import commands
from contextlib import redirect_stdout


class Eval(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.result = ""


    def escape_quote(self, content):
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        return content.strip('` \n')

#evaluation
    @commands.command(aliases = ["evaluate", "exe", "execute"], pass_context=True)
    @commands.is_owner()
    async def eval(self, ctx, *, body: str):
        env = {
            'client': self.client,
            'ctx': ctx,
            'self': self,
            '_': self.result
        }

        env.update(globals())

        body = self.escape_quote(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            evem = discord.Embed(title = "", description = f"`Result`\n```py\n{e.__class__.__name__}: {e}\n```")
            return await ctx.send(embed = evem)

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            evem = discord.Embed(title = "", description = f'`Result`\n```py\n{value}{traceback.format_exc()}\n```')
            await ctx.send(embed = evem)
        else:
            value = stdout.getvalue()

            if ret is None:
                if value:
                    evem = discord.Embed(title = "", description = f'`Result`\n```py\n{value}\n```')
                    await ctx.send(embed = evem)

            else:
                self.result = ret
                evem = discord.Embed(title = "", description = f'`Result`\n```py\n{value}{ret}\n```')
                await ctx.send(embed = evem)


def setup(client):
    client.add_cog(Eval(client))


