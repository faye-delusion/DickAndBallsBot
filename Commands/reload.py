import discord
from discord import slash_command

from discord.ext import commands

import os


async def reload(bot, ctx, extension:str = None):

    if extension == None:

        commands_ = []
        events = []

        for file in os.listdir("Commands"):

            if file.endswith(".py"):

                filename = file[:-3]

                bot.reload_extension(f"Commands.{filename}")

                commands_.append(filename)

            for file in os.listdir("Events"):

                if file.endswith(".py"):

                    filename = file[:-3]

                    bot.reload_extension(f"Events.{filename}")

                    events.append(filename)

            embed = discord.Embed(

                title="All extensions reloaded.",
                colour=discord.Colour.random()

            )

            embed.add_field(name="Commands", value="{}".format('\n'.join(commands_)))
            embed.add_field(name="Events", value="{}".format('\n'.join(events)))

            bot.register_commands()

            return embed

    else:

        ex = discord.ApplicationCommand

        try:

            ex = bot.reload_extension(f"Commands.{extension}")
            await bot.register_commands()

        except:

            try:

                ex = bot.reload_extension(f"Events.{extension}")
                 
            except:

                return discord.Embed(

                    title=f"Extension {extension} not found.",
                    colour=discord.Colour.random()

                )

            else:

                return discord.Embed(

                    title=f"Extension {extension} reloaded.",
                    colour=discord.Colour.random()

                )

        else:

            return discord.Embed(

                title=f"Extension {extension} reloaded.",
                colour=discord.Colour.random()

            )

class reload_(commands.Cog):

    def __init__(self,bot):

        self.bot = bot

    @commands.command(name="reload")
    @commands.is_owner()
    async def reload_chat(self,ctx,extension: str = None):

        output = await reload(self.bot, ctx, extension) 

        await ctx.reply(embed=output)

    @slash_command(name="reload", guild_ids=[817475690499670066])
    @commands.is_owner()
    async def reload_slash(self,ctx,extension: discord.Option(str) = None):

        output = await reload(self.bot, ctx, extension)

        await ctx.respond(embed=output, ephemeral=True)

def setup(bot):

    bot.add_cog(reload_(bot))