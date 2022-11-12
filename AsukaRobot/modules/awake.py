import asyncio
import telegram
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from AsukaRobot.events import register
from AsukaRobot import telethn as borg, OWNER_ID, OWNER_NAME
from AsukaRobot import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins
from pyrogram import __version__ as pyro


edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/6cbc8452a2796ad58c2f9.jpg"
file2 = "https://telegra.ph/file/3b4eed00be4dfaa189fff.jpg"
file3 = "https://telegra.ph/file/0b5e88c90238c357641a7.jpg"
file4 = "https://telegra.ph/file/4e964395ea9138c943dce.jpg"
""" =======================CONSTANTS====================== """

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@register(pattern=("Hey ayaka"))
async def hmm(yes):
    chat = await yes.get_chat()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    Asuka = f"۞ **Hᴇʏ [{yes.sender.first_name}](tg://user?id={yes.sender.id}) I'ᴍ Aʏᴀᴋᴀ**\n"
    
    Asuka += f"۞ **Mʏ Uᴘᴛɪᴍᴇ** - `{uptime}`\n"
    
    Asuka += f"۞ **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ** - `{version.__version__}`\n"
    
    Asuka += f"۞ **PTB Vᴇʀsɪᴏɴ** - `{telegram.__version__}`\n"
    
    Asuka += f"۞ **Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ** - `{pyro}`\n"
    
    Asuka += f"۞ **Mʏ Mᴀsᴛᴇʀ** - [ARAN](tg://user?id={OWNER_ID})\n\n"
    Asuka += f"Tʜᴀɴᴋs Fᴏʀ Aᴅᴅɪɴɢ Mᴇ Iɴ {yes.chat.title}"
    BUTTON = [[Button.url("Support Chat", "https://t.me/mysticbots_support"), Button.url("Updates", "https://t.me/AyakaUpdates")]]
    on = await borg.send_file(yes.chat_id, file="https://telegra.ph/file/f1e36934d02cded4a1776.mp4",caption=Asuka, buttons=BUTTON)
