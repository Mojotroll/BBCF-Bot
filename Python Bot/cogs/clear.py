import discord
from discord.ext import commands

class clear(commands.Cog):

    def __init__(self, client):
        self.client = client

        @commands.command()
        @commands.has_permissions(manage_messages=True)
        async def clear(ctx, amount : int):
            await ctx.channel.purge(limit=amount)


def setup(client):
    client.add_cog(clear(client))