import discord
from discord.ext import commands
from Model.model import *

class Notebook(commands.Cog):
    def __init__(self, client, model: Model):
        self.client = client
        self.model = model

    @commands.Cog.listener()
    async def on_ready(self):
        print('Command notebook ready')

    @commands.command(name='nb', aliases=['NB'], ignore_extra=False)
    async def command_notebook(self, ctx, action='', target=''):
        action = action.upper()
        target = target.upper()

        def check(m):
            return m.author == ctx.author

        if action == 'PEEK':
            desc = None

            if target == 'TEAM':
                desc = self.model.getStudentsFromSubject(ctx.guild.id, ctx.channel.category.name)
            elif target == 'NOTE':
                desc = self.model.getNotesFromSubject(ctx.guild.id, ctx.channel.category.name)
            elif target == 'LINK':
                desc = self.model.getLinksFromSubject(ctx.guild.id, ctx.channel.category.name)
            else:
                # Unknown target
                raise commands.BadArgument()

            # Send info
            await ctx.send(embed=discord.Embed(
                title='Notebook command',
                description=desc,
                colour=self.model.getDefaultColor()
            ))
        # ---------------------------------------------
        elif action == 'WRITE':
            if target == 'NOTE':
                name = None
                text = None

                # Ask for name
                embed = discord.Embed(
                    title='Notebook command',
                    description='Send a message with the name of the note.',
                    colour=self.model.getDefaultColor()
                )
                embed.set_footer(text='Timeout in 20 seconds!')
                await ctx.send(embed=embed)

                try:
                    msg = await self.client.wait_for('message', timeout=20.0, check=check)
                    name = msg.content
                except:
                    # Timeout
                    raise commands.BadArgument()

                # Ask for content
                embed = discord.Embed(
                    title='Notebook command',
                    description='Send a message with the content of the note.',
                    colour=self.model.getDefaultColor()
                )
                embed.set_footer(text='Timeout in 60 seconds!')
                await ctx.send(embed=embed)

                try:
                    msg = await self.client.wait_for('message', timeout=60.0, check=check)
                    text = msg.content
                except:
                    # Timeout
                    raise commands.BadArgument()

                # Output
                if self.model.addNoteToSubjectFromGuild(ctx.guild.id, ctx.channel.category.name, name, text):
                    embed = discord.Embed(
                        title='Notebook command',
                        description='Note successfully saved.',
                        colour=self.model.getDefaultColor()
                    )
                else:
                    embed = discord.Embed(
                        title='Notebook command',
                        description='Note failed to be saved.',
                        colour=self.model.getDefaultColor()
                    )

                await ctx.send(embed=embed)
            elif target == 'LINK':
                name = None
                url = None
                
                # Ask for name
                embed = discord.Embed(
                    title='Notebook command',
                    description='Send a message with the name of the link.',
                    colour=self.model.getDefaultColor()
                )
                embed.set_footer(text='Timeout in 20 seconds!')
                await ctx.send(embed=embed)

                try:
                    msg = await self.client.wait_for('message', timeout=20.0, check=check)
                    name = msg.content
                except:
                    # Timeout
                    raise commands.BadArgument()

                # Ask for url
                embed = discord.Embed(
                    title='Notebook command',
                    description='Send a message with the content of the note.',
                    colour=self.model.getDefaultColor()
                )
                embed.set_footer(text='Timeout in 20 seconds!')
                await ctx.send(embed=embed)

                try:
                    msg = await self.client.wait_for('message', timeout=20.0, check=check)
                    url = msg.content
                except:
                    # Timeout
                    raise commands.BadArgument()

                # Output
                if self.model.addLinkToSubjectFromGuild(ctx.guild.id, ctx.channel.category.name, name, url):
                    embed = discord.Embed(
                        title='Notebook command',
                        description='Link successfully saved.',
                        colour=self.model.getDefaultColor()
                    )
                else:
                    embed = discord.Embed(
                        title='Notebook command',
                        description='Link failed to be saved.',
                        colour=self.model.getDefaultColor()
                    )

                await ctx.send(embed=embed)
            else:
                # Unknown target
                raise commands.BadArgument()
        # ---------------------------------------------
        elif action == 'ERASE':
            if target == 'NOTE':
                index = None
                
                # Ask for index
                embed = discord.Embed(
                    title='Notebook command',
                    description='Send a message with the id of the note.',
                    colour=self.model.getDefaultColor()
                )
                embed.set_footer(text='Timeout in 20 seconds!')
                await ctx.send(embed=embed)

                try:
                    msg = await self.client.wait_for('message', timeout=20.0, check=check)
                    index = msg.content
                except:
                    # Timeout
                    raise commands.BadArgument()

                # Verify
                if not index.isdigit():
                    raise commands.BadArgument()
                else:
                    index = int(index)

                # Output
                if self.model.removeNoteOfSubjectFromGuild(ctx.guild.id, ctx.channel.category.name, index):
                    embed = discord.Embed(
                        title='Notebook command',
                        description='Note successfully removed.',
                        colour=self.model.getDefaultColor()
                    )
                else:
                    embed = discord.Embed(
                        title='Notebook command',
                        description='Note failed to be removed.',
                        colour=self.model.getDefaultColor()
                    )

                await ctx.send(embed=embed)
            elif target == 'LINK':
                index = None
                
                # Ask for index
                embed = discord.Embed(
                    title='Notebook command',
                    description='Send a message with the id of the link.',
                    colour=self.model.getDefaultColor()
                )
                embed.set_footer(text='Timeout in 20 seconds!')
                await ctx.send(embed=embed)

                try:
                    msg = await self.client.wait_for('message', timeout=20.0, check=check)
                    index = msg.content
                except:
                    # Timeout
                    raise commands.BadArgument()

                # Verify
                if not index.isdigit():
                    raise commands.BadArgument()
                else:
                    index = int(index)

                # Output
                if self.model.removeLinkOfSubjectFromGuild(ctx.guild.id, ctx.channel.category.name, index):
                    embed = discord.Embed(
                        title='Notebook command',
                        description='Link successfully removed.',
                        colour=self.model.getDefaultColor()
                    )
                else:
                    embed = discord.Embed(
                        title='Notebook command',
                        description='Link failed to be removed.',
                        colour=self.model.getDefaultColor()
                    )

                await ctx.send(embed=embed)
            else:
                # Unknown target
                raise commands.BadArgument()
        else:
            # Unknown action
            raise commands.BadArgument()
