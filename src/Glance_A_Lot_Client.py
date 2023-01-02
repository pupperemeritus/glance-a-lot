import discord


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
            f"You can drop a message in this dm if you are feeling down",
        )

    async def on_message(self, message):
        """Function that processes message"""
        if message.author == self.client.user:
            return
        if message.content.startsWith("$w"):
            pass
        if message.content.startsWith("$s"):
            pass
        if message.content.startsWith("$r"):
            pass
        if message.content.startsWith("$"):
            pass

    async def on_message_edit(self, message):
        pass
