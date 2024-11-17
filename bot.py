from bale import Bot, Update, Message
import asyncio

client = Bot(token="1353433662:gkyMC4m7CKzWbcg3d6FIqST15ZIxoOXt9BXUPObU")

@client.event
async def on_ready():
    print(client.user, "is Ready!")

@client.event
async def on_update(update: Update):
    print(update)

@client.event
async def on_message(message: Message):
    await message.reply(text="Hi!")

async def main():
    while True:
        await client.poll_updates()
        await asyncio.sleep(3)  

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
