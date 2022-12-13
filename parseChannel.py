import telethon
from telethon import events

client = telethon.TelegramClient("session", api_id=14695876, api_hash="3b7a9c4d1c0caa734d13c8985ce40e95")

client.start()

@client.on(events.NewMessage(chats=('WeblancerJobsBot')))
async def handler(event):
  print(event.message.text)

client.run_until_disconnected()