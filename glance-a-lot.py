from setup import *
from src import *
import os
import dotenv

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
guildName = os.getenv("GUILD")

client = Glance_A_Lot_Client.Glance_A_Lot_Client(guildName)
client.run(TOKEN)
