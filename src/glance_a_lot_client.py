"""Contains the client class"""
import sqlite3 as sql

import discord

import src.emotion_detection_model_loader as ed
import src.weather as wtr
from src.search import search_engine


class GlanceALotClient(discord.Client):
    """Contains the code for the glance-a-lot client."""

    def __init__(self, intents):
        super().__init__(intents=intents)
        self.conn = sql.connect('glancealot.db')

    async def on_ready(self):
        """A function that is called when bot is connected to discord."""
        print("Bot is ready")

    async def on_member_join(self, member):
        """Function that checks for new members joining and sends them a welcome message."""
        await member.create_dm()
        await member.dm_channel.send(
            f"Hello {member.name}, I hope you are doing fine. Welcome to my Discord server\n",
            "You can drop a message in this dm if you are feeling down",
        )

    async def on_message(self, message):
        """Function that processes message."""
        print("On message called")
        print(message)
        print(message.author, message.content)
        if message.author == "glancealot#8890":
            return
        if message.content.startswith("glance wthr"):
            print("weather")
            city = message.content[13:]
            try:
                resp = await wtr.OWMWeather.get_weather(city)
                print(resp)
                await message.channel.send(resp)
            except Exception as e:
                await message.channel.send(e)
        elif message.content.startswith("glance srch"):
            print("search")
            await message.channel.send(search_engine(message.content[12:].split()[0],
                                                     message.content[12+len(message.content[12:].split()[0]):]))
        print("method end")

    async def on_message_edit(self, before, after):
        """Function that processes message edit."""
        if after.content.startswith("glance"):
            self.on_message(after.content)
