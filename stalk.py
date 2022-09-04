from pyrogram import Client, filters, idle
from pyrogram.types import Message
from os import getenv
from database import *

API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = getenv("OWNER_ID")

app = (":Yashvi:", API_ID, API_HASH, BOT_TOKEN)

@app.on_message(filters.command(["unstalk", "stalk"]))
    sudo = await is_sudo(m.from_user.id)
    if not sudo:
        return
    if m.text.split()[0][1].lower() == "u":
        stalking = await stalking(m.from_user.id)
        if not stalking:
            return await 
