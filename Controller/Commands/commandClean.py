import discord
from discord.ext import commands

class Clean(commands.Cog):
    def __init__(self, client, model):
        self.client = client
        self.model = model

    @commands.Cog.listener()
    async def on_ready(self):
        print('Command clean ready')

    @commands.command(name='clean', aliases=['CLEAN'], ignore_extra=False)
    @commands.has_role('BotManager')
    async def command_help(self, ctx, amount=10):
        def check(m):
            return True

        deleted = await ctx.channel.purge(limit=amount,check=check)
        await ctx.send(embed=discord.Embed(
            title='Clean command',
            description=f'Deleted {len(deleted)} messages.',
            colour=self.model.getDefaultColor()
        ))
