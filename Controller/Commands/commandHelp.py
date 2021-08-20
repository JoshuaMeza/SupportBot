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
        prefix = self.model.getPrefix()

        embed = discord.Embed(
            title='Commands list',
            description='**NOTE:** Commands with a lock requires a role called "BotManager".',
            colour=self.model.getDefaultColor()
        )

        if arg == '':
            embed.add_field(
                name='Help',
                value='The help command brings information about all the commands.\n'
                    f'**{prefix}help**: List of all commands.\n'
                    f'**{prefix}help logs**: List of all logs commands.\n'
                    f'**{prefix}help user**: List of all users commands.\n'
                    f'**{prefix}help nb**: List of all notebook commands.',
                inline=False
            )
        elif arg == 'LOGS':
            embed.add_field(
                name='Logs',
                value='The logs command manages the registered subjects.\n'
                    f'🔒**{prefix}logs add**: Add the actual category as a subject.\n'
                    f'🔒**{prefix}logs del**: Delete the actual category as a subject.',
                inline=False
            ) # TODO: The guild shall be added automatically
        elif arg == 'USER':
            embed.add_field(
                name='User',
                value='The user command modifies user information.\n'
                    f'**{prefix}user add [@user]**: Add a team member to the current subject.\n'
                    f'🔒**{prefix}user del [@user]**: Delete a team member from the current subject.\n'
                    f'**{prefix}user mod [@user]**: Modify info of a team member in the entire guild.',
                inline=False
            ) # TODO: Mod will require something like a UI, just continue asking the info
        elif arg == 'NB':
            embed.add_field(
                name='Notebook',
                value='The notebook command helps to create and access easily to the current subject info.\n'
                    f'**{prefix}nb peek team**: Peek the information of the team members.\n'
                    f'**{prefix}nb peek note**: Peek the team saved notes.\n'
                    f'**{prefix}nb peek link**: Peek the team saved links.\n'
                    f'**{prefix}nb write [note/link]**: Write in the notebook.\n'
                    f'**{prefix}nb erase [note/link]**: Erase something from the notebook.',
                inline=False
            )
        else:
            raise commands.BadArgument()
                
        embed.set_footer(text=ctx.guild.name)
        await ctx.send(embed=embed)
