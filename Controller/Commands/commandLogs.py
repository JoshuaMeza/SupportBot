import discord
from discord.ext import commands
from Model.model import *

class Logs(commands.Cog):
    def __init__(self, client, model: Model):
        self.client = client
        self.model = model

    def __verRole(self, roles):
        flag = False

        for role in roles:
            if role.name == self.model.getLockRoleName():
                flag = True
                break
    
        return flag

    @commands.Cog.listener()
    async def on_ready(self):
        print('Command logs ready')

    @commands.command(name='logs', aliases=['LOGS'], ignore_extra=False)
    async def command_logs(self, ctx, arg: str):
        arg = arg.upper()
        desc = None

        if arg == 'ADD' or arg == 'DEL':
            # Role required
            if self.__verRole(ctx.author.roles):
                # Add
                if arg == 'ADD':
                    if self.model.addSubjectToGuild(ctx.guild.id, ctx.channel.category.name):
                        desc = 'Category successfully added as a subject.'
                    else:
                        desc = 'Category failed to be added as a subject.'
                # Delete
                else:
                    if self.model.removeSubjectOfGuild(ctx.guild.id, ctx.channel.category.name):
                        desc = 'Subject successfully deleted.'
                    else:
                        desc = 'Subject failed to be deleted.'
            else:
                raise commands.MissingRole(self.model.getLockRoleName())
        elif arg == 'VFY':
            # Verify
            if self.model.containsSubject(ctx.guild.id, ctx.channel.category.name):
                desc = 'This category have been registered as a subject.'
            else:
                desc = 'This category haven\'t been registered as a subject yet.'
        else:
            raise commands.BadArgument()

        await ctx.send(embed=discord.Embed(
            title='Logs command',
            description=desc,
            colour=self.model.getDefaultColor()
        ))
