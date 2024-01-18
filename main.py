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

approve_mode = False  # Initial state of approval mode

@app.on_message(filters.command("approvejoin") & filters.private)
async def toggle_approval(client, message):
    global approve_mode
    approve_mode = not approve_mode  # Toggle the boolean value

    await message.reply(f"Join request approval is now {'on' if approve_mode else 'off'}.")

@app.on_chat_join_request()
async def handle_join_request(client, chat_join_request):
    if approve_mode:
        try:
            await client.approve_chat_join_request(chat_join_request.chat.id, chat_join_request.from_user.id)
            await client.send_message(chat_join_request.chat.id, "Join request approved automatically. Welcome!")

            # Send a direct message to the new user
            await client.send_message(chat_join_request.from_user.id, "Hey there! I've approved your join request. Glad to have you in the group!")
        except Exception as e:
            await client.send_message(chat_join_request.chat.id, f"Failed to approve join request: {e}")
    else:
        await client.send_message(chat_join_request.chat.id, "Join request pending manual approval.")

@app.on_message(filters.command("waifu"))
async def send_waifu(client, message):
    try:
        url = 'https://api.waifu.im/search'
        params = {'included_tags': ['maid'], 'height': '>=2000'}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            random_image_url = data['images'][0]['url']  # Select a random image
            await client.send_photo(message.chat.id, random_image_url)
        else:
            await message.reply("Failed to fetch image from Waifu.im.")
    except Exception as e:
        await message.reply(f"An error occurred: {e}")

print("hello, I am alive!!")
app.run()
