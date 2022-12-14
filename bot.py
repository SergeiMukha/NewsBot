import aiogram
import asyncio
import telethon
from telethon import events
import os

client = telethon.TelegramClient("session", api_id=14695876, api_hash="3b7a9c4d1c0caa734d13c8985ce40e95")

bot = aiogram.Bot("5632955841:AAEVBqx1PH8fojYl6PGwBtACi9kGQ6gSTHI")
dp = aiogram.Dispatcher(bot)

client.start()

@client.on(events.NewMessage(chats=('oko_original')))
async def handler(event):

    message = event.message

    message.text = message.text.replace("[ПОДПИСАТЬСЯ](https://t.me/+ZU_MUdIOlIs2ZDMy) ✅ [Прислать контент](https://t.me/Info_ukraine_bot)", "")

    if message.video:
        await client.send_file(entity=-1001685738658, file=message.video, caption=message.text)
    elif message.photo:
        await client.send_file(entity=-1001685738658, file=message.photo, caption=message.text)
    
client.run_until_disconnected()

