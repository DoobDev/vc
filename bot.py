# Doob Dev
import discord
import json
import asyncio
import logging
import os

from discord.ext import commands
# These just came with Doob Bot, if not needed will remove later.

owner_id = "308000668181069824"

# Creates and loads the json file.
def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)

client.remove_command("help")

@client.event
async def on_ready():
    print('VC is online!')
    await client.change_presence(status = discord.Status.online, activity=discord.Game('vc/help for commands. | github.com/mmatt625/vc'))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Missing Requirement Error [DB10]", description="Pass in all required arguments.", colour=discord.Color.blue())

        await ctx.send(embed=embed)

    
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="Missing Permissions Error [DB11]", description="You are not able to use this command because you do not have the required permissions.", colour=discord.Color.blue())

        await ctx.send(embed=embed)

# Opens json file then dumps '-'
@client.event
async def on_guild_join(self, guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "vc/"

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

# Removes guild from json file when Doob leaves.
@client.event
async def on_guild_remove(self, guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.command(aliases=['vc', 'screenshare', 'ss'])
async def vcshare(ctx):
    embed = discord.Embed(title="Screenshare", description="Cilck this link to screenshare", colour=discord.Color.blue())

    embed.add_field(name="Screenshare here", value=f"https://discordapp.com/channels/{ctx.guild.id}/{ctx.author.voice.channel.id}")

    await ctx.send(embed=embed)

@client.command(aliases=["upvote"])
async def vote(ctx):
    embed = discord.Embed(title="Vote", description="Vote on VC bot on...", colour=discord.Color.blue())

    embed.add_field(name="Top.gg", value="https://top.gg/bot/706286009771360310/vote")

    await ctx.send(embed=embed)

@client.command()
async def ping(ctx, self):
    embed = discord.Embed(title="Pong!", description=":ping_pong:", colour=discord.Color.blue())

    embed.add_field(name="The latency for VC is...", value=f"{round(self.client.latency * 1000)} ms")

    await ctx.send(embed=embed)

# Changes the prefix (that the user provides.) for the specific server.
@client.command(aliases=['prefix'])
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    embed = discord.Embed(title="An administrator has changed the prefix.", description=f"An administrator has changed the prefix to {prefix}.", colour=discord.Color.blue())

    embed.add_field(name="The prefix has been changed to:", value=prefix)
    await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def ownerprefixchange(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    embed = discord.Embed(title="An owner of VC has changed the prefix.", description=f"The owner has changed the prefix to {prefix}.", colour=discord.Color.blue())

    embed.add_field(name="The prefix has been changed to:", value=prefix)
    await ctx.send(embed=embed)

client.run("token")
