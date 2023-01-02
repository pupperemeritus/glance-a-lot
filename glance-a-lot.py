<<<<<<< HEAD
import src.emotionDetection
import src.reminders
import src.serverStats
import src.weather
import src.webSearch
=======
from setup import *
from src import *
import os
import dotenv

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
guildName = os.getenv("GUILD")

client = Glance_A_Lot_Client.Glance_A_Lot_Client(guildName)
client.run(TOKEN)
>>>>>>> e09c3eaa2bab7bdd31f4d92e2e05c3cc98ff7bf2
