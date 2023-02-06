"""Contains the client class"""
import sqlite3 as sql

import discord

import src.emotion_detection_model_loader as ed
import src.Weather as wtr


class Glance_A_Lot_Client(discord.Client):
    """Contains the code for the glance-a-lot client."""

    def __init__(self, guildName):
        self.client = discord.Client()
        self.guildName = guildName

    async def on_ready(self):
        """A function that is called when bot is connected to discord."""
        guild = discord.utils.get(self.client.guilds, name=self.guildName)
        print(f"{self.client.user} has connected to Discord via the following guild")
        print(f"Name{guild.name}   ID:{guild.id}")

    async def on_member_join(self, member):
        """Function that checks for new members joining and sends them a welcome message."""
        await member.create_dm()
        await member.dm_channel.send(
            f"Hello {member.name}, I hope you are doing fine. Welcome to my Discord server\n",
            "You can drop a message in this dm if you are feeling down",
        )

    async def on_message(self, message):
        """Function that processes message."""
        if message.author == self.client.user:
            return
        if message.content.startsWith("glance wthr"):
            city = message.content[13:]
            weather_object = wtr.OWMWeather()
            await self.channel.send(weather_object.get_weather(city))
        if message.content.startsWith("glance srch"):
            pass
        if not message.content.startsWith("glance"):
            emotion_detection_obj = ed.EmotionDetection()
        

    async def on_message_edit(self, message):
        """Function that processes message edit."""
        if message.content.startsWith("glance"):
            self.on_message(message)
