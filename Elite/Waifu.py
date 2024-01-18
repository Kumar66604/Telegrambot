import pyrogram
import requests
from ..main import app

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

