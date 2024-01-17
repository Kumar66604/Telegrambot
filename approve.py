import pyrogram
from main import app

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
            await client.send_message(chat_join_request.chat.id, "Join request approved automatically.")
        except Exception as e:
            await client.send_message(chat_join_request.chat.id, f"Failed to approve join request: {e}")
    else:
        await client.send_message(chat_join_request.chat.id, "Join request pending manual approval.")

print("BOT SUCCESSFULLY DEPLOYED !!")

app.run()
