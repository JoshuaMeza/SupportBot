import discord
from discord.ext import commands
from Model.model import *

class User(commands.Cog):
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
        print('Command user ready')

    @commands.command(name='user', aliases=['USER'], ignore_extra=False)
    async def command_user(self, ctx, action: str, target: discord.Member):
        action = action.upper()
        desc = None

        def check(m):
            return m.author == ctx.author

        if action == 'ADD':
            if self.model.addStudentToSubjectFromGuild(ctx.guild.id, ctx.channel.category.name, target.id):
                desc = 'Student successfully added to this subject.'
                self.model.editStudentNamesFromGuild(ctx.guild.id, target.name, target.id)
            else:
                desc = 'Student failed to be added to this subject.'
        elif action == 'MOD':
            options = ['NAME','LNAME','ID','EMAIL','NUMBER']
            option = None
            data = None

            # Ask for option
            embed = discord.Embed(
                title='Notebook command',
                description='Send a message with an option:\n'
                            '[name/lname/id/email/number]',
                colour=self.model.getDefaultColor()
            )
            embed.set_footer(text='Timeout in 20 seconds!')
            await ctx.send(embed=embed)

            try:
                msg = await self.client.wait_for('message', timeout=20.0, check=check)
                option = msg.content.upper()
                if not option in options: raise Exception()
            except:
                # Timeout
                raise commands.BadArgument()

            # Ask for content
            embed = discord.Embed(
                title='Notebook command',
                description='Send a message with the new information.',
                colour=self.model.getDefaultColor()
            )
            embed.set_footer(text='Timeout in 30 seconds!')
            await ctx.send(embed=embed)

            try:
                msg = await self.client.wait_for('message', timeout=30.0, check=check)
                data = msg.content
            except:
                # Timeout
                raise commands.BadArgument()

            # Output
            if option == options[0]:
                # Name
                if self.model.editStudentNamesFromGuild(ctx.guild.id, data, target.id):
                    desc = 'Name successfully modified.'
                else:
                    desc = 'Name failed to be modified.'
            elif option == options[1]:
                # Last name
                if self.model.editStudentLastNamesFromGuild(ctx.guild.id, data, target.id):
                    desc = 'Last name successfully modified.'
                else:
                    desc = 'Last name failed to be modified.'
            elif option == options[2]:
                # Id
                if not data.isdigit():
                    raise commands.BadArgument()
                else:
                    data = int(data)

                if self.model.editStudentCollegeIdFromGuild(ctx.guild.id, data, target.id):
                    desc = 'Id successfully modified.'
                else:
                    desc = 'Id failed to be modified.'
            elif option == options[3]:
                # Email
                if self.model.editStudentEmailFromGuild(ctx.guild.id, data, target.id):
                    desc = 'Email successfully modified.'
                else:
                    desc = 'Email failed to be modified.'
            elif option == options[4]:
                # Number
                if not data.isdigit():
                    raise commands.BadArgument()
                else:
                    data = int(data)
                
                if self.model.editStudentPhoneNumberFromGuild(ctx.guild.id, data, target.id):
                    desc = 'Phone number successfully modified.'
                else:
                    desc = 'Phone number failed to be modified.'
            else:
                raise commands.BadArgument()
        elif action == 'DEL':
            if self.__verRole(ctx.author.roles):
                if self.model.removeStudentOfSubjectFromGuild(ctx.guild.id, ctx.channel.category.name, target.id):
                    desc = 'Student successfully deleted from this subject.'
                else:
                    desc = 'Student failed to be deleted from this subject.'
            else:
                raise commands.MissingRole(self.model.getLockRoleName())
        else:
            # Unknown action
            raise commands.BadArgument()

        await ctx.send(embed=discord.Embed(
            title='User command',
            description=desc,
            colour=self.model.getDefaultColor()
        ))
