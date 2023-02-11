"""Main module"""
import discord
import dotenv

import src.glance_a_lot_client as galc

if __name__ == '__main__':
    dotenv.load_dotenv(dotenv.find_dotenv(".env"))
    TOKEN = dotenv.dotenv_values()["DISCORD_TOKEN"]
    intents = discord.Intents(messages=True, guilds=True,message_content=True)
    client = galc.GlanceALotClient(intents)
    client.run(TOKEN)
