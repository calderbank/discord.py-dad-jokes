import requests
import discord
import os
import random


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


    if message.content.startswith('.dadjoke'):
      joke = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "text/plain"}).text
      await message.channel.send (joke)
    await client.process_commands(message)
    
    
