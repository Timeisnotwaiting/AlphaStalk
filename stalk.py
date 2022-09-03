from pyrogram import Client, filters, idle
from pyrogram.types import Message
from os import getenv
from database import *

API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = getenv("OWNER_ID")

app = (":Yashvi:", API_ID, API_HASH, BOT_TOKEN)

@app.on_message(filters.command("stalk"))
