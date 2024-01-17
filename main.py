from pyrogram import Client, filters

app = Client(
    "Test-Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text("Hello! I am your bot. How can I help you?")

print("BOT SUCCESSFULLY DEPLOYED !!")

app.run()
