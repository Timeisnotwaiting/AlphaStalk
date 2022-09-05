from pyrogram import Client
from pyrogram.types import Message

async def Log(t):
    log = get_log()
    return await Client.send_message(log, t)
