import discord
from discord.ext import commands
import sqlite3

class cf(commands.cog):

    def __init__(self, client):
        self.client = client

    @bbcf.command()
    async def char(self):
        """See All Available Blazblue Characters in Database"""
        conn = sqlite3.connect('Database/Data.db')
        c = conn.cursor()
        commands = c.execute("select name from sqlite_master where type = 'table'")
        if not commands:
            await client.say("No Characters were found, please contact Bot Owner")
        else:
            embed = discord.Embed()
            embed.title = "Blazblue Central Fiction"
            embed.add_field("Available Commands", value=commands)

            await client.say(embed=embed)

    @bbcf.command()
    async def charmoves(self, *, character):
        """See All Available Moves for Character in Database"""
        conn = sqlite3.connect('Database/Data.db')
        c = conn.cursor()
        commands = c.execute("select DISTINCT ID from " + str(character))
        if not commands:
            await client.say('No Commands found for specified Character, please verify name was spelled correctly or contact the Bot Owner')
        else:
            embed = discord.Embed()
            embed.title = "Move list for " + character
            embed.add_field("Available Commands", value=commands)

            await client.say(embed=embed)
			
	@bbcf.command()
	async def find (self, *, character, move):
		"""Search for a character move in Database"""
		conn = sqlite3.connect('Database/Data.db')
		c = conn.cursor()
		commands = c.execute('select * from ' + str(character) + ' WHERE ID = ' + str(move))
		data = commands.fetchall()
		if data == None:
			await client.say('No Results found, please confirm the spelling for the Character and Move.')
				
			

    
