import discord
from discord.ext import commands

class vc(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Gives user the link to screenshare on Discord without using Go Live.
    @commands.command(aliases=['vcshare', 'screenshare', 'ss'])
    async def vc(self, ctx):
        embed = discord.Embed(title="Screenshare", description="Cilck this link to screenshare", colour=discord.Color.blue(), url=f"https://discordapp.com/channels/{ctx.guild.id}/{ctx.author.voice.channel.id}")

        embed.add_field(name="Screenshare here", value=f"https://discordapp.com/channels/{ctx.guild.id}/{ctx.author.voice.channel.id}")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(vc(client))