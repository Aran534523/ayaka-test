from AsukaRobot import pgram

@BOT.on(events.NewMessage(incoming=True, pattern=r"\%svoid(?: |$)(.*)" % hl))

async def void(event):

    PHOTO="https://telegra.ph/file/e5808adf6d1bc748d6440.jpg"

    Text= f"""

Welcome to [【V๏ɪ፝֟𝔡】Network](https://t.me/voidxnetwork)

━━━━━━━━━━━━━━━━━━━━━━

✪ ᴠᴏɪᴅ ɪꜱ ᴀɴ ᴀɴɪᴍᴇ ʙᴀꜱᴇᴅ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴡɪᴛʜ ᴀ ᴍᴏᴛɪᴠᴇ ᴛᴏ ꜱᴘʀᴇᴀᴅ ʟᴏᴠᴇ ᴀɴᴅ ᴘᴇᴀᴄᴇ ᴀʀᴏᴜɴᴅ ᴛᴇʟᴇɢʀᴀᴍ.

✪ ɢᴏ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴊᴏɪɴ ᴛʜᴇ ᴄᴏᴍᴍᴜɴɪᴛʏ ɪꜰ ɪᴛ ᴅʀᴀᴡꜱ ʏᴏᴜʀ ᴀᴛᴛᴇɴᴛɪᴏɴ. 

━━━━━━━━━━━━━━━━━━━━━━

"""

    await BOT.send_file(event.chat_id,

                PHOTO,

                caption=Text,

                buttons=(

                [

                    [Button.url("【V๏ɪ፝֟𝔡】Network", "https://t.me/VoidXNetwork")],

                    [

                    Button.url("【ᴜꜱᴇʀᴛᴀɢ】", "https://t.me/VoidxNetwork/136"),

                    Button.url("【ɪɴᴅᴇx】", "https://t.me/VoidxNetwork/15")

                    ],

                ]

            ),

        )
