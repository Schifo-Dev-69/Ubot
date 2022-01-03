from telethon.sync import TelegramClient, events
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon import TelegramClient


api_id = 12138400
api_hash = 'e4d75abe5ed054bf7139f1251d9e2163'
client = TelegramClient(StringSession('1BJWap1wBu12qc71JFiIffIC3Wp7sSMmoLoQVomSvk1uO8M4aHtn1cLIX7CLJaMT1ZfoVbdsqHzOOvv1fts-nOWExcD5CXhBMk2OnGWcrCMuF2J3tbXG0ZEdTYL6JmoZC8yeZsyZtBqNs_TydZZSLSGUqvZihoS0aEnvNUv9b4yelIGqGFZ904SK1U0bhODcHyjtOxVtggqg3M67kvAV-4fubO07w3jkiH17lreaUJChH5C1gWXtGw5hVdeupqXP0n9qlIZIuOM1U0Rnop_-rckN0gKQAkRp1Hc1rWGO8MHXrPdrD4vAM7KMXKSma83WuJcqVIsNFehz_5o7nE9Rb9PR1KpflZBI='), api_id, api_hash)
string = '1BJWap1wBu12qc71JFiIffIC3Wp7sSMmoLoQVomSvk1uO8M4aHtn1cLIX7CLJaMT1ZfoVbdsqHzOOvv1fts-nOWExcD5CXhBMk2OnGWcrCMuF2J3tbXG0ZEdTYL6JmoZC8yeZsyZtBqNs_TydZZSLSGUqvZihoS0aEnvNUv9b4yelIGqGFZ904SK1U0bhODcHyjtOxVtggqg3M67kvAV-4fubO07w3jkiH17lreaUJChH5C1gWXtGw5hVdeupqXP0n9qlIZIuOM1U0Rnop_-rckN0gKQAkRp1Hc1rWGO8MHXrPdrD4vAM7KMXKSma83WuJcqVIsNFehz_5o7nE9Rb9PR1KpflZBI='
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