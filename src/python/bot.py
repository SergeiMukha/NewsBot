import os 
import aiogram
import telethon
from telethon import events
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv("BOT_TOKEN_PYTHON")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

# Create Client
client = telethon.TelegramClient("session", api_id=API_ID, api_hash=API_HASH)

# Create Bot
bot = aiogram.Bot(BOT_TOKEN)
dp = aiogram.Dispatcher(bot)

# Start Client
client.start()

# Tracking For New Messages In Certain Chat
@client.on(events.NewMessage(chats=('oko_original')))
async def handler(event):

    message = event.message

    # Removing Unnecessary Text
    message.text = message.text.replace("[ПОДПИСАТЬСЯ](https://t.me/+ZU_MUdIOlIs2ZDMy) ✅ [Прислать контент](https://t.me/Info_ukraine_bot)", "")

    # Checking If There Is a Photo or a Video in Message 
    if message.video:
        await client.send_file(entity=-1001685738658, file=message.video, caption=message.text)
    elif message.photo:
        await client.send_file(entity=-1001685738658, file=message.photo, caption=message.text)

# Running Client
print("Bot Has Been Started")
client.run_until_disconnected()

