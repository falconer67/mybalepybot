from balethon import Client

bot = Client("1353433662:gkyMC4m7CKzWbcg3d6FIqST15ZIxoOXt9BXUPObU")

replies = {
    "hello": "Hi",
    "hi": "Hey!",
    "how are you": "Fine thanks! And You?",
    "bot": "Yes, how can I help you?",
    "haha": "What's so funny?",
    "bye": "Good bye!"
}


@bot.on_command()
async def start(*, message):
    texts = "\n".join(replies)
    await message.reply(
        f"Send one of the following texts to me and I will reply:\n{texts}"
    )


@bot.on_command()
async def learn(text, reply, *, message):
    replies[text] = reply

    await message.reply(
        f"I got it\nWhen someone says {text}, I say {reply}"
    )


@bot.on_message(lambda client, event: event.text in replies)
async def reply_to_text(message):
    await message.reply(replies[message.text])


bot.run()
