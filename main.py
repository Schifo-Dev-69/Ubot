from pyrogram import Client
from pyrogram import filters

app = Client("my_account", config_file="configuration.ini")
@app.on_message(filters.command("info", "."))
async def info(Client, message):

    user = await app.get_users( message.text.split(" ")[1])

    print(user)
    await message.edit (f"info di {user.first_name}\n\nid: {user.id}")

@app.on_message(filters.command("lol","."))
async def info(client,message):
    await message.edit("Il ridere , la burla , il meme , il kek , il divertimento , la goliardia , la ridaranza , la risata fragorosa , la battuta goliardica , la burla italiana , lo scherzo all'italiana , l'ilarità,  lo scherzo goliardico , la risata a crepapelle , la letizia , il funesto intrattenimento del ridere , il manifestarsi di un sentimento di allegrezza mediante modificazione del ritmo reapiratorio e variazione della mimica facciale anche denominato divertimento , la situazione usuale alla quale ognuno di noi ha assistito almeno una volta nella propria vita descritta tramite immagini e scritte , il ridere , la comicità , la fumettistica , il simpatismo , la risacca , il funny , lo spasso , il buffo , la farsa , la beffa , la burla , il divertimento , la pagliaccieria , l'azione giullaresca.")
@app.on_message(filters.command("a","."))
async def info(client,message):
    await message.edit("ᵃ")
    
    

@app.on_message(filters.command("hi", "."))
async def hi(Client, message):

   await app.send_message(message.chat.id, "hi")

@app.on_message(filters.command("stop", "."))
async def stoppa(Client, message):

   await app.send_message(message.chat.id, "Userbot **stopped** as succesfull!")
   sys.exit()

app.run()

