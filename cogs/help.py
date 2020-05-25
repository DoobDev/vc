import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, client):
        self.client = client
    # Decorator for commands.
    @commands.command(aliases=['helpme'])
    async def help(self, ctx):
        embed = discord.Embed(title="Command Help", description="All of VC's commands.", colour=discord.Color.blue())

        embed.add_field(name="Check out the docs!", value="https://www.notion.so/doob/VC-Commands-d925cea5bab6425189dd57ff5eb923b3")
        embed.add_field(name="Join the Support Discord", value="https://discord.gg/ryTYWjD")

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(help(client))
