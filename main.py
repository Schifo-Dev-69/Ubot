from pyrogram import Client, filters
from pyrogram.types import Message

app = Client("my_account", config_file="configuration.ini")


@app.on_message(filters.command("info", ".") & filters.me)
async def info(client: Client, message: Message):
    username = message.text.split(" ")[1]
    try:
        user = await client.get_users(username)
    except:
        await message.edit_text("L'username {username} non è occupato da nessun utente")
        return
    print(user)
    await message.edit_text(f"Info di {user.first_name}\n\nid: {user.id}")

    
@app.on_message(filters.command("lol",".") & filters.me)
async def info(client: Client, message: Message):
    await message.username("Il ridere , la burla , il meme , il kek , il divertimento , la goliardia , la ridaranza , la risata fragorosa , la battuta goliardica , la burla italiana , lo scherzo all'italiana , l'ilarità,  lo scherzo goliardico , la risata a crepapelle , la letizia , il funesto intrattenimento del ridere , il manifestarsi di un sentimento di allegrezza mediante modificazione del ritmo reapiratorio e variazione della mimica facciale anche denominato divertimento , la situazione usuale alla quale ognuno di noi ha assistito almeno una volta nella propria vita descritta tramite immagini e scritte , il ridere , la comicità , la fumettistica , il simpatismo , la risacca , il funny , lo spasso , il buffo , la farsa , la beffa , la burla , il divertimento , la pagliaccieria , l'azione giullaresca.")


@app.on_message(filters.command("a",".") & filters.me)
async def info(client: Client, message: Message):
    await message.username("ᵃ")


@app.on_message(filters.command("hi", ".") & filters.me)
async def hi(client: Client, message: Message):
   await message.reply_text("hi")


@app.on_message(filters.command("stop", ".") & filters.me)
async def stoppa(client: Client, message: Message):
   await message.reply_text("Userbot **stopped** as succesfull!")
   sys.exit()

app.run()

