from telethon.sync import TelegramClient, events
from telethon import TelegramClient

from telethon import TelegramClient

# Remember to use your own values from my.telegram.org!
api_id = 12138400
api_hash = 'e4d75abe5ed054bf7139f1251d9e2163'
client = TelegramClient('anon', api_id, api_hash)

async def my_event_handler(event):
    if 'hello' in event.raw_text:
        await event.reply('hi!')
        @client.on(events.NewMessage(outgoing=True, pattern=r'\.save'))
        async def handler(event):
             if event.is_reply:
                  replied = await event.get_reply_message()
        sender = replied.sender
        await client.download_profile_photo(sender)
        await event.respond('Saved your photo {}'.format(sender.username))