"""Main module"""
import dotenv

import src.glance_a_lot_client as client

dotenv.load_dotenv(dotenv.find_dotenv(".env"))
DISCORD_GUILD = dotenv.dotenv_values()["DISCORD_GUILD"]
clnt = client.GlanceALotClient(DISCORD_GUILD)
