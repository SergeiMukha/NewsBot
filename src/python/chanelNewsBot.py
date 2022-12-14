import os
import telethon
from telethon import events
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
CHAT_ID = int(os.getenv("CHAT_ID_PYTHON"))
PARSING_CHAT = os.getenv("PARSING_CHAT")

# Create Client
client = telethon.TelegramClient("session", api_id=API_ID, api_hash=API_HASH)

# Start Client
client.start()

# Tracking For New Messages In Certain Chat
@client.on(events.NewMessage(chats=(PARSING_CHAT)))
async def handler(event):

    message = event.message

    # Removing Unnecessary Text
    message.text = message.text.replace("[ПОДПИСАТЬСЯ](https://t.me/+ZU_MUdIOlIs2ZDMy) ✅ [Прислать контент](https://t.me/Info_ukraine_bot)", "")

    # Checking If There Is a Photo or a Video in Message 
    if message.video:
        await client.send_file(entity=CHAT_ID, file=message.video, caption=message.text)
    elif message.photo:
        await client.send_file(entity=CHAT_ID, file=message.photo, caption=message.text)
    else:
        await client.send_message(entity=CHAT_ID, message=message.text)

# Running Client
print("Bot Python Has Been Started")
client.run_until_disconnected()

