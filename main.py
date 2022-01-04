from pyrogram import Client

app = Client("my_account", config_file="my_configuration.ini")

@app.on_message(filters.command("info", "."))
async def info(Client, message):

    user = await app.get_users( message.text.split(" ")[1])

    print(user)
    await app.send_message(message.chat.id, f"info di {user.first_name}\n\nid: {user.id}")

app.run()