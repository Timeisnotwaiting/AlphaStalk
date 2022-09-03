from pyrogram import Client, filters, idle
from pyrogram.types import Message
from os import getenv

API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = getenv("OWNER_ID")

app = (":Yashvi:", API_ID, API_HASH, BOT_TOKEN)

