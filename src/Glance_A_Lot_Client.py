import discord
import src.weather as wtr
import src.Search as search
import src.Reminders as rmndrs
import src.EmotionDetection as ed
import sqlite3 as sql


class Glance_A_Lot_Client(discord.Client):
    def __init__(self, guildName):
        self.client = discord.Client()
        self.guildName = guildName

    async def on_ready(self):
        """A function that is called when bot is connected to discord"""
        guild = discord.utils.get(self.client.guilds, name=self.guildName)
        print(f"{self.client.user} has connected to Discord via the following guild")
        print(f"Name{guild.name}   ID:{guild.id}")

    async def on_member_join(self, member):
        """Function that checks for new members joining and sends them a welcome message"""
        await member.create_dm()
        await member.dm_channel.send(
            f"Hello {member.name}, I hope you are doing fine. Welcome to my Discord server\n",
            "You can drop a message in this dm if you are feeling down",
        )

    async def on_message(self, message):
        """Function that processes message"""
        if message.author == self.client.user:
            return
        if message.content.startsWith("glance wthr"):
            try:
                cityCountry = message.content[14:]
                city = []
                country = []
                commaFlag = False
                for i in cityCountry:
                    if i == ",":
                        commaFlag = True
                    if commaFlag is True:
                        country.append(i)
                    else:
                        city.append(i)
                city = str(city)
                country = str(country)
            except IndexError:
                message.channel.send(
                    "Enter valid command, separate city and country using comma"
                )
        if message.content.startsWith("glance srch"):
            pass
        if message.content.startsWith("glance remd"):
            pass
        if message.content.startsWith("glance stat"):
            pass

    async def on_message_edit(self, message):
        pass
