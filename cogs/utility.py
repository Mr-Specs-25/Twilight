import json
import discord
import json
from neuralintents import GenericAssistant

from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    def load_json_intents(self, intents):
        self.intents = json.loads(open(intents).read())

    ai = GenericAssistant("intents.json")
    ai.train_model()
    ai.save_model()

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.client.user == message.author:
                return
        if self.client.user.mentioned_in(message):
            response = ai.request(message.content)
            await message.channel.send(response, reference = message)


def setup(client):
    client.add_cog(Utility(client))

