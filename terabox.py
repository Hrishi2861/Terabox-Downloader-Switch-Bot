from swibots import Client, BotCommand, BotContext, CommandEvent, InlineMarkup, InlineKeyboardButton, MessageEvent
import requests
import logging
import aria2p
import os
from dotenv import load_dotenv

load_dotenv('config.env', override=True)

bot_token = os.environ.get('BOT_TOKEN', '')
if len(bot_token) == 0:
    logging.error("BOT_TOKEN variable is missing! Exiting now")
    exit(1)

app = Client(bot_token, "Jet-Terabox-Downloader-Switch-Bot 🚀❤️")

aria2 = aria2p.API(
    aria2p.Client(
        host="http://localhost",
        port=6800,
        secret=""
    )
)
options = {
    "max-tries": "50",
    "retry-wait": "3",
    "continue": "true"
}

aria2.set_global_options(options)

logging.basicConfig(level=logging.INFO)

app.set_bot_commands([BotCommand("start", "Get start message", True)])


@app.on_command("start")
async def onStart(ctx: BotContext[CommandEvent]):
    await ctx.event.message.reply_text(
        f"Hi, I am {ctx.user.creator_name}!\n ɪ ᴀᴍ ᴀ ᴛᴇʀᴀʙᴏx ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ʙᴏᴛ. sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴛᴇʀᴀʙᴏx ʟɪɴᴋ ɪ ᴡɪʟʟ ᴅᴏᴡɴʟᴏᴀᴅ ᴡɪᴛʜɪɴ ғᴇᴡ sᴇᴄᴏɴᴅs ᴀɴᴅ sᴇɴᴅ ɪᴛ ᴛᴏ ʏᴏᴜ ✨.",
        inline_markup=InlineMarkup(
            [[InlineKeyboardButton("ᴊᴏɪɴ ❤️🚀", url="https://myswitch.click/Asy3")],[InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ ⚡️", url="https://telegram.me/hrishikesh2861")]]
        ),
    )

@app.on_message()
async def handle_message(ctx: BotContext[MessageEvent]):
    message = ctx.event.message    
    url = getattr(message, 'text', None) or getattr(message, 'body', None) or getattr(message, 'message', None)

    if not url:
        await message.reply_text("❌ ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴀ ᴠᴀʟɪᴅ ᴍᴇssᴀɢᴇ.")
        return

    user_mention = ctx.user.creator_name
    user_id = ctx.user.parent_id

    try:
        reply_msg = await message.reply_text("sᴇɴᴅɪɴɢ ʏᴏᴜ ᴛʜᴇ ᴍᴇᴅɪᴀ...🤤")

        response = requests.get(f"https://teraboxvideodownloader.nepcoderdevs.workers.dev/?url={url}")
        response.raise_for_status()
        data = response.json()

        resolutions = data["response"][0]["resolutions"]
        fast_download_link = resolutions["Fast Download"]
        thumbnail_url = data["response"][0]["thumbnail"]
        video_title = data["response"][0]["title"]

        download = aria2.add_uris([fast_download_link])

        while download.is_active:
            download.update()

        if download.is_complete:
            file_path = download.files[0].path

            thumbnail_path = "thumbnail.jpg"
            thumbnail_response = requests.get(thumbnail_url)
            with open(thumbnail_path, "wb") as thumb_file:
                thumb_file.write(thumbnail_response.content)

            await reply_msg.delete()

            logging.info(f"Sending media to user {user_id} with file_path: {file_path}")
            
            response = await app.send_media(
            document=file_path,
            caption=f"🎬 ᴛɪᴛʟᴇ: {video_title}\nʟᴇᴇᴄʜᴇᴅ ʙʏ: {user_mention}",
            user_id=user_id,
            thumb=thumbnail_path,
            part_size=100*1024*1024,
            task_count=30)
            # inline_markup=InlineMarkup(
            #     [[InlineKeyboardButton("ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ", text="This feature is be Added Soon!")]]))
            os.remove(file_path)
            os.remove(thumbnail_path)
        else:
            raise Exception("Download failed")

    except Exception as e:
        logging.error(f"Error fetching video: {e}")
        await message.reply_text(f"❌ ᴇʀʀᴏʀ!! ᴇɴᴛᴇʀ ᴀ ᴠᴀʟɪᴅ ᴛᴇʀᴀʙᴏx ᴜʀʟ.")

app.run()