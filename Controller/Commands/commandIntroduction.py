import discord
from discord.ext import commands
from Model.model import *

class Introduction(commands.Cog):
    def __init__(self, client, model: Model):
        self.client = client
        self.model = model

    @commands.Cog.listener()
    async def on_ready(self):
        print('Command introduction ready')

    @commands.command(name='intro', aliases=['INTRO'], ignore_extra=False)
    @commands.has_role('BotManager')
    async def command_introduction(self, ctx):
        await ctx.message.delete()

        embed = discord.Embed(
            title='Introduction command',
            description='Welcome! I\'m going to be helping you during your stay in this lobby.\n'
            f'For more information about the commands you can try **{self.model.getPrefix()}help**.',
            colour=self.model.getDefaultColor()
        )

        embed.add_field(
            name='Lobby goal',
            value='Have a common place in where everyone can work and communicate with their teammates in '
                'an efficient way, taking advantage of the disponibility of a text chat, a voice chat and '
                'some bots to do some tasks.',
            inline=False
        )

        embed.add_field(
            name='Lobby rules',
            value='We are college students already, so please avoid:\n'
                '1. Spamming.\n'
                '2. Trolling in harmful ways.\n'
                '3. Being excessively rude.\n'
                '4. Avoid helping with the team\'s homework.',
            inline=False
        )

        embed.add_field(
            name='Instructions to members',
            value='As you should know, you belong to a defined number of subjects of the lobby, '
                'so if you don\'t have your special role to access that channel, please ask '
                'for some help.\n'
                'Once you can access your channel (subject), *enter to it* and then verify with the '
                ' *notebook* command if you have been registered, if not, you can do it by yourself '
                'using the *add* action of the *user* command. The next step is to register your '
                'academic information (this have to be done just once, your profile is persistent), '
                ' which is done with the *mod* action of the *user* command.\n'
                '**Note:** Names, Last names, and Email are strings; Id and Phone number are integers.',
            inline=False
        )

        embed.add_field(
            name='How do I help you at all?',
            value='I have a variety of commands, the ones you could use more are the *notebook* commands, '
            'which specialize in retreaving your teammate\'s registered information and check, create and '
            'remove the notes and links that the team saved.\n'
            'Also, the information is private and unique among all the subjects.',
            inline=False
        )

        embed.set_image(url='https://images.pexels.com/photos/6207368/pexels-photo-6207368.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940')
        embed.set_footer(text=ctx.guild.name)
        await ctx.send(embed=embed)
