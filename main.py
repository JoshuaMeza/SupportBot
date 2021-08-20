"""
Author Joshua I. Meza Magaña
Date 16/08/2021
Version 0.1.0
A bot which helps with team organization.
"""
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
#from controller.keepAlive import *
from Model.model import *
from Controller.Commands.commandHelp import *

# Variables
model = Model()

# Bot specs
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=model.getPrefix(), intents=intents)
client.remove_command('help')

# Events
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author != client.user:
        await client.process_commands(message)

@client.event
async def on_command_error(ctx, error):
    embed = discord.Embed
    errColor = model.getErrorColor()

    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title='Command Error',
            description='I don\'t recognize your command.',
            colour=errColor
        )
    elif isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title='Cooldown Error',
            description='This command is on cooldown, try again later.',
            colour=errColor
        )
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title='Permissions Error',
            description='You don\'t have enough permissions to execute that command.',
            colour=errColor
        )
    elif isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.BadArgument) or isinstance(error, commands.TooManyArguments):
        embed = discord.Embed(
            title='Arguments Error',
            description='You are giving incorrect parameters.',
            colour=errColor
        )
    elif isinstance(error, commands.DisabledCommand):
        embed = discord.Embed(
            title='Status Error',
            description='You tried to use a disabled command.',
            colour=errColor
        )
    else:
        embed = discord.Embed(
            title='Undefined Error',
            description='Something unexpected happend...',
            colour=errColor
        )
        print(error)

    embed.set_footer(text=f'Use the command {model.getPrefix()}help for more information.')
    await ctx.send(embed=embed, delete_after=30.0)

        
# Activate web host
#keep_alive()

# Adding commands
if model.getCommandHelpStatus():
    client.add_cog(Help(client, model))

# Activate bot
load_dotenv()
client.run(os.getenv('TOKEN'))