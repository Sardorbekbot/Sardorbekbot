import time
from datetime import datetime
from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

# Replace 'your_api_id', 'your_api_hash', and 'your_phone_number' with your actual details
api_id = 26609245
api_hash = 'e01e5bc9be494189e34236e920da50e4'
phone = '+996

client = TelegramClient('session_name', api_id, api_hash)

async def update_nickname():
    while True:
        current_time = datetime.now().strftime('%H:%M')
        full_name = f'your_name | {current_time}'
        try:
            await client(UpdateProfileRequest(first_name=full_name))
            print(f"Nickname updated to: {full_name}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(60)  # Wait 60 seconds before updating again

async def main():
    await update_nickname()

with client:
    client.loop.run_until_complete(main(
