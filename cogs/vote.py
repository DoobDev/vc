import discord
from discord.ext import commands

class vote(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["upvote"])
    async def vote(self, ctx):
        embed = discord.Embed(title="Vote", description="Vote on VC bot on...", colour=discord.Color.blue())

        embed.add_field(name="Top.gg", value="https://top.gg/bot/706286009771360310/vote")

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(vote(client))
