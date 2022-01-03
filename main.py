from telethon.sync import TelegramClient, events
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon import TelegramClient


api_id = 12138400
api_hash = 'e4d75abe5ed054bf7139f1251d9e2163'
client = TelegramClient(StringSession(string), api_id, api_hash)

print("Avvio userbot...")
client.start()
print("Userbot avviato!")
client.run_until_disconnected()

@client.on(events.NewMessage(outgoing=True))
async def info(event):
     x = await event.get_reply_message()
     if event.text == ".info":
             if x.sender.bot == True:
                is_bot = "✔"
             elif x.sender.bot == False:
                is_bot = "✖"
             await event.edit(f"INFORMAZIONI SULL'UTENTE\nNome: {x.sender.first_name}\nID: » <code>{x.sender.id}</code>\nBot: {is_bot}\nUsername: {x.sender.username}\nDC: {x.sender.photo.dc_id}",parse_mode="html")
             lol