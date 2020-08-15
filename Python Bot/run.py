import discord
from discord.ext import commands
from discord.ext import tasks
import os
from itertools import cycle
import sqlite3
from urllib.request import pathname2url

#Modified Variables and Other information used by the bot
serverPrefix = '.'
ownerID = ''

def ownerCheck(ctx):
    return ctx.author.id == ownerID

botToken = ''

client = commands.Bot(command_prefix=serverPrefix)
status = ['Blazblue Central Fiction', 'Blazblue Cross Tag Battle', 'Guilty Blue Revelator Gear Blaze-rd', "Susano'o Best Waifu", "Accent Phantasma, BlazCore", "Blazblue 4 Ultimax", "Under Naoto Izayoi aegisBlade", "Tager Gives The Best Hugs", "Mai giving out free handies"]

###############################################################################################################################
###########################################Owner Specific Commands############################################################
@client.command()
@commands.check(ownerCheck)
async def load(ctx, extension):
    client.load_extension('cogs.{extension}')

@client.command()
@commands.check(ownerCheck)
async def unload(ctx, extension):
    client.unload_extension('cogs.{extension}')

@client.command()
@commands.check(ownerCheck)
async def reload(ctx, extension):
    client.unload_extension('cogs.{extension}')
    client.load_extension('cogs.{extension}')

#############################################################################################################################################
################################ Bot Start Up Code  #########################################################################################


#Loads Cogs on Start up

for fileName in os.listdir('./cogs'):
    if fileName.endswith('.py'):
        client.load_extension('cogs.{fileName[:-3]}')

#Checks to see if the DB is Present and Creates it loading the schema if not found.

if not os.path.exists('Data.db'):
    conn = sqlite3.connect('Database/Data.db')

    with open('./data/schema.sql') as sch:
        conn.executescript(sch.read())

#@client.event
#async def on_command_error(ctx, error):
#    if isinstance(error, commands.MissingRequiredArgument):
#        await ctx.send('Missing Argument, please include missing information!')

@client.command()
async def commands(ctx):
        conn = sqlite3.connect('Database/Data.db')
        c = conn.cursor()
        c.execute("select name from sqlite_master where type = 'table'")

############################# Ready Check for Bot and a Status update using the status list #################################################

@clients.event
async def on_ready():
    print("Bot is Ready")
    change_status.start()
    await client.change_presence(status=discord.Status.online, activity=discord.game(change_status()))

@tasks.loop(hour=1)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

########################Runs the bot using token provided######################################################################

client.run(botToken)
