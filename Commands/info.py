import discord
from discord import slash_command
from discord.ext import commands

import sys
import os
import psutil

import json


async def info(ctx, bot):

    bot_author = bot.get_user(265152100575477760)

    embed = discord.Embed(

        title="Dick and Balls Bot Info",
        description=f"**Written by: {bot_author.mention}**",
        colour=discord.Colour.random()
        
    )

    embed.set_thumbnail(url=bot.user.avatar.url)

    last_restart = json.load(open("config.json", "r"))["last_restart"]

    embed.add_field(

        name="Last Restart",
        value=f"<t:{int(last_restart)}>\n<t:{int(last_restart)}:R>",
        inline=True

    )

    embed.add_field(

        name="Guilds",
        value=f"`{len(bot.guilds)}`",
        inline=True
    
    )

    embed.add_field(

        name="Users",
        value=f"`{len(bot.users)}`",
        inline=True

    )

    embed.add_field(

        name="Active Voice Connections",
        value=f"`{len(bot.voice_clients)}`",
        inline=True

    )

    embed.add_field(

        name="System Memory Usage",
        value=f"`{psutil.virtual_memory().percent}%\n {round(psutil.virtual_memory().used / (1024. ** 3), 2)}/{round(psutil.virtual_memory().total / (1024. ** 3), 2)}GB`",
        inline=True
    )

    embed.add_field(

        name="System CPU Usage",
        value=f"`{psutil.cpu_percent()}%`",
        inline=True

    )

    embed.add_field(

        name="Python Version",
        value=f"`Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}`",
        inline=True

    )

    return embed

class info_(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @slash_command(

        name="info"

    )
    async def info_slash(self,ctx):

        output = await info(ctx, self.bot)

        await ctx.respond(embed=output)

    @commands.command(

        name="info"

    )
    async def info_chat(self,ctx):

        output = await info(ctx, self.bot)

        await ctx.respond(embed=output)

def setup(bot):
    bot.add_cog(info_(bot))