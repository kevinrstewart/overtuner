import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message_text = message.content.strip().lower()

    if "overtuned" in message_text or "over tuned" in message_text:
        await message.channel.send(f"{message.author.mention} I think you mean overpowered")

client.run('')