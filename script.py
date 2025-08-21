from telethon.sync import TelegramClient
import asyncio
import random
import time

api_id = 25631095
api_hash = '9baaa3bc642284375c4fda63823896a5'
session_name = 'anon'

messages = [
    "",
    "",
    "",
    "",
    "",
    ""
    ""
    ""
]

target_chat = '@NftParserRebot'

async def main():
    async with TelegramClient(session_name, api_id, api_hash) as client:
        while True:
            msg = random.choice(messages)
            await client.send_message(target_chat, msg)
            await asyncio.sleep(random.uniform(0.5, 2))  

asyncio.run(main())
