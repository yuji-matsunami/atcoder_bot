# This example requires the 'message_content' intent.
import os
from dotenv import load_dotenv
import discord
from scraping import get_contest

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$contest'):
        contest = get_contest()
        await message.channel.send(f'@everyone\n次のコンテストは{contest[1]}です。\n{contest[0]}開始です。')

load_dotenv()
client.run(os.environ['token'])
