from pyrogram import Client
from pyrogram.types import Message

async def Log(t):
    get_log()
    await Client.send_message(
