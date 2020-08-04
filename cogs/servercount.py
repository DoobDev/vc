import dbl
import discord
from discord.ext import commands

dbltoken = input("Input your Top.gg token.\n")
class servercount(commands.Cog):
   # Decorator events.
    def __init__(self, client):
        self.client = client
        self.token = dbltoken # set this to your DBL token
        self.dblpy = dbl.DBLClient(self.client, self.token, autopost=True) # Autopost will post your guild count every 30 minutes
        print("uploaded top.gg")


def setup(client):
    client.add_cog(servercount(client))
