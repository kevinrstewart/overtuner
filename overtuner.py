import discord

from discord.utils import get

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--key', required=True, help='The key to use to connect to the bot on Discord')
parser.add_argument('--react', dest='react', default=False, action='store_true')
args = parser.parse_args()

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
        emoji = get(message.guild.emojis, name='clippy')
        if args.react:
            await message.add_reaction(emoji)
        else:
            await message.channel.send(f"{message.author.mention} I think you mean overpowered")

client.run(args.key)