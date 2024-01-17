import os
from pyrogram import Client, filters
from Config import *

for file in os.listdir():
    if file.endswith(".session"):
        os.remove(file)
for file in os.listdir():
    if file.endswith(".session-journal"):
        os.remove(file)
       

app = Client(
    "Test-Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text("Hello! I am your bot. How can I help you?")

approve_mode = False

@app.on_message(filters.command("approvejoin") & filters.private)
async def toggle_approval(client, message):
    global approve_mode
    approve_mode = not approve_mode  # Toggle the boolean value

    await message.reply(f"Join request approval is now {'on' if approve_mode else 'off'>

@app.on_chat_join_request()
async def handle_join_request(client, chat_join_request):
    if approve_mode:
        try:
            await client.approve_chat_join_request(chat_join_request.chat.id, chat_join>

        except Exception as e:
            await client.send_message(chat_join_request.chat.id, f"Failed to approve jo>
    else:
        await client.send_message(chat_join_request.chat.id, "Join request pending manu>


print("BOT SUCCESSFULLY DEPLOYED !!")

app.run()
