from traceback import format_exception
import discord
from discord import slash_command
from discord.ext import commands, tasks

import asyncio
import requests
import os
import sys
import json
import io
import contextlib
import textwrap

def clean_code(content):

    if content.startswith("```") and content.endswith("```"):

        return '\n'.join(content.split("\n")[1:])[:-3]

    else:

        return content

async def evaluate(self,ctx,code, uncleancode):

    local_variables = {

        "discord": discord,
        "commands": commands,
        "tasks": tasks,
        "bot": self.bot,
        "ctx": ctx,
        "asyncio": asyncio,
        "requests": requests,
        "os": os,
        "sys": sys,
        "json": json,
        "io": io

    }

    stdout = io.StringIO()

    try:

        with contextlib.redirect_stdout(stdout):

            exec(

                f"async def func():\n{textwrap.indent(code, '    ')}", local_variables
            )

            obj = await local_variables["func"]()
            result = f"{stdout.getvalue()}\n"

    except Exception as e:

        result = "".join(format_exception(e,e,e.__traceback__))

        return discord.Embed(

            title="Big fuckin oopsie something went wrong!",
            description=f"Input\n```py\n{uncleancode}```\nOutput\n```py\n{result}```",
            colour=discord.Colour.red()

        )

    else:

        if len(result) <= 1:

            return

        else:

            return discord.Embed(

                description=f"Input\n```py\n{uncleancode}```\nOutput\n```py\n{result}```",
                colour=discord.Colour.green()

            )

class eval_(commands.Cog):

    def __init__(self,bot):

        self.bot = bot

    @slash_command(

        name="eval",
        description="Owner only eval command"

    )
    @commands.is_owner()
    async def eval_slash(self,ctx,*, code):

        uncleancode = code
        code = clean_code(code)

        output = await evaluate(self,ctx,code,uncleancode)

        await ctx.respond("<:fistbump:839245908323598387>",embed=output)

    @commands.command(

        name="eval"

    )
    @commands.is_owner()
    async def eval_text(self,ctx,*,code):

        uncleancode = code
        code = clean_code(code)

        output = await evaluate(self,ctx,code,uncleancode)

        await ctx.reply("<:fistbump:839245908323598387>", embed=output)

def setup(bot):
    bot.add_cog(eval_(bot))