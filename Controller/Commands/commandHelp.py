import discord
from discord.ext import commands
from Model.model import *

class Help(commands.Cog):
    def __init__(self, client, model: Model):
        self.client = client
        self.model = model

    @commands.Cog.listener()
    async def on_ready(self):
        print('Command help ready')

    @commands.command(name='help', aliases=['HELP'], ignore_extra=False)
    async def command_help(self, ctx, arg = ''):
        arg = arg.upper()
        embed = discord.Embed(
            title='Help command',
            description='You can use the following commands.',
            colour=self.model.getDefaultColor()
        )

        embed.add_field(
                name='List',
                value=f'**{self.model.getPrefix()}help**: List of all commands'
            )
                
        embed.set_footer(text=ctx.guild.name)
        await ctx.send(embed=embed)
