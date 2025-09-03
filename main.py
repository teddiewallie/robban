import discord_client, INTENTS from discord.py
import TOKEN from secrets.py

def main():
    client = DiscordClient(intents=INTENTS)
    client.run(TOKEN)
