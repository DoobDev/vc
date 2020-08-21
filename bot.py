# Doob Dev
import discord
import json
import os

from discord.ext import commands

token = input("Input your Discord Bot Token.\n")

# Creates and loads the json file.
def get_prefix(client, message)
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    try:
         return prefixes[str(message.guild.id)]
    except KeyError:
         return 'vc/'

client = commands.Bot(command_prefix = get_prefix)

client.remove_command("help")

@client.event
async def on_ready()
    print('VC is online!'
    await client.change_presence(status = discord.Status.online, activity=discord.Game('vc/help for commands. | github.com/doobdev/vc'))

@client.command()
async def load(ctx, extension):
    print(f'Loaded {extension}')
    client.load_extension(f'cogs.{extension}')
    print(f'Loaded {extension}')

@client.command()
async def unload(ctx, extension):
    print(f'Unloaded {extension}')
    client.unload_extension(f'cogs.{extension}')
    print(f'Unloaded {extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
