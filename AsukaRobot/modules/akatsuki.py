@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sakatsuki(?: |$)(.*)" % hl))

async def akatsuki(event):

    PHOTO="https://telegra.ph/file/af1d6556f7ce3a402528f.mp4"

    Text= f"""

Welcome to [Akatsuki Network](https://t.me/Akatsukixnetwork)

━━━━━━━━━━━━━━━━━━━

۞ ᴀᴋᴀᴛsᴜᴋɪ ɪꜱ ᴀɴ ᴀɴɪᴍᴇ ʙᴀꜱᴇᴅ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴡɪᴛʜ ᴀ ᴍᴏᴛɪᴠᴇ ᴛᴏ ꜱᴘʀᴇᴀᴅ ʟᴏᴠᴇ ᴀɴᴅ ᴘᴇᴀᴄᴇ ᴀʀᴏᴜɴᴅ ᴛᴇʟᴇɢʀᴀᴍ.

۞ ɢᴏ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴊᴏɪɴ ᴛʜᴇ ᴄᴏᴍᴍᴜɴɪᴛʏ ɪꜰ ɪᴛ ᴅʀᴀᴡꜱ ʏᴏᴜʀ ᴀᴛᴛᴇɴᴛɪᴏɴ. 

━━━━━━━━━━━━━━━━━━━

"""

    await BOT.send_file(event.chat_id,

                PHOTO,

                caption=Text,

                buttons=(

                [

                    [Button.url("ᴀᴋᴀᴛsᴜᴋɪ ɴᴇᴛᴡᴏʀᴋ", "https://t.me/AkatsukiXNetwork")],

                    [

                    Button.url("ᴛᴀɢ", "https://t.me/twork/136"),

                    Button.url("ɪɴᴅᴇx", "https://t.me/Vwok/15")

                    ],

                ]

            ),

        )
