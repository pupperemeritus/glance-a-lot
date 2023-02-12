"""Contains the client class"""
import discord
import pymongo

from src.emotion_detection_model_loader import EmotionDetection
import src.weather as wtr
from src.search import search_engine
from random import choices


class GlanceALotClient(discord.Client):
    """Contains the code for the glance-a-lot client."""

    def __init__(self, intents):
        super().__init__(intents=intents)
        self.dbclient = pymongo.MongoClient(host="localhost:27017", port=27017)
        self.db = self.dbclient.get_database("glancealot")
        self.userNegDet = self.db.get_collection("userNegativeDetects")
        print(self.dbclient.server_info() != "")

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
        if str(message.author) == "glancealot#8890":
            return
        if message.content.startswith("glance wthr"):
            print("weather")
            city = message.content[11:]
            try:
                resp = wtr.OWMWeather.get_weather(city)
                print(resp)
                await message.channel.send(resp)
            except Exception as e:
                await message.channel.send(e)
        elif message.content.startswith("glance srch"):
            print("search")
            await message.channel.send(search_engine(message.content[12:].split()[0],
                                                     message.content[12+len(message.content[12:].split()[0]):]))
        else:
            message_emotion = EmotionDetection.message(message.content)
            print(message_emotion)
            if message_emotion in ("sadness", "anger", "fear"):
                if self.userNegDet.find_one({"user": str(message.author)}) is None:
                    self.userNegDet.insert_one({
                        "user": str(message.author),
                        "sad_count": 1
                    })
                else:
                    old = self.userNegDet.find_one(
                        {"user": str(message.author)})
                    if old["sad_count"] <= 2:
                        print(self.userNegDet.update_one(
                            {"user": str(message.author)},
                            {"$inc": {"sad_count": 1}}
                        ).modified_count != 0)
                    elif old["sad_count"] > 2:
                        print(self.userNegDet.delete_one(
                            {"user": str(message.author)}).deleted_count != 0)
                        await message.channel.send(
                            "I hope you can make it through this tough time")
                        cheer = ['/meme', '/xkcd', '/animals']
                        choice = choices(cheer)[0]
                        await message.channel.send("You can type " + choice + " to ease your mind by  looking at " + choice[1:])
        print("method end")

    async def on_message_edit(self, before, after):
        """Function that processes message edit."""
        if after.content.startswith("glance"):
            self.on_message(after.content)
