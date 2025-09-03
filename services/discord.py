import discord

class discord_client(discord.client):
    async def on_ready(self):
        print("Logged on as {self.user}.")

    async def on_message(self, message):
        # message.author
        # message.content

INTENTS = discord.Intents.default()
INTENTS.message_content = True

