from pyrogram import Client
import os

log = os.getenv("LOG_ID")

async def Log(t):
    return await Client.send_message(log, t)

