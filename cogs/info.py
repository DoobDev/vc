import discord
from discord.ext import commands

class info(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Gives user some info about VC
    @commands.command(aliases=['botinfo'])
    async def info(self, ctx):
        embed = discord.Embed(title="VC's Info", description="Some of VC's info that might be useful for you to know!", colour=discord.Color.blue())

        embed.add_field(name="Name", value="VC")
        embed.add_field(name="Description", value="VC is a bot that gives you the Screenshare link for your server / vc channel.")
        embed.add_field(name="Developer", value="The creator of VC is <@308000668181069824>")
        embed.add_field(name="Hosted on", value="AWS Server")
        embed.add_field(name="Bot's Server Count", value=f"{str(len(self.client.guilds))}")
        embed.add_field(name="Bot's Member Count", value=f"{str(len(self.client.users))}")
        embed.add_field(name="The ping for VC is...", value=f" :ping_pong: {round(self.client.latency * 1000)} ms")
        embed.add_field(name="Library", value="discord.py")
        embed.add_field(name="Top.gg Link", value="https://top.gg/bot/706286009771360310")
        embed.add_field(name="Invite Link", value="https://discordapp.com/oauth2/authorize?client_id=706286009771360310&scope=bot&permissions=3072")
        embed.add_field(name="GitLab Repository", value="https://github.com/doobdev/vc")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(info(client))

