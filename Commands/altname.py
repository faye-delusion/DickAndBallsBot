import discord
from discord import slash_command
from discord.ext import commands

import json
import requests
import random

with open("config.json", "r") as f:

    config = json.load(f)

guilds = config["test_guilds"]

async def generate_alt(ctx):

    adj = requests.get("https://random-word-form.herokuapp.com/random/adjective")
    noun = requests.get("https://random-word-form.herokuapp.com/random/noun")

    if adj.status_code == 200 and noun.status_code == 200:

        adj_json = adj.json()
        noun_json = noun.json()

        embed = discord.Embed(

            title=f"{adj_json[0].title()}{noun_json[0].title()}{random.randint(0,9999)}",
            colour=discord.Colour.random()

        )

        return embed

    else:

        return discord.Embed(

            title="Something went wrong. :(",
            description="The random word API is probably down, blame them.",
            colour=discord.Colour.random()

        )

aliases = [

    "alt_name",
    "alt",
    "generatealt",
    "generate_alt"

]

class generate_alt_(commands.Cog):

    def __init__(self,bot):

        self.bot = bot

    @commands.command(name="altname", aliases=aliases)
    async def altname_chat(self,ctx):

        msg = await ctx.send(embed=discord.Embed(title="Generating alt name, please be patient.", colour=discord.Colour.random()))

        output = await generate_alt(ctx)

        await msg.edit(embed=output)

    @slash_command(name="alt", guild_ids=guilds)
    async def altname_slash(self,ctx,viewable: discord.Option(bool) = True):

        output = await generate_alt(ctx)

        await ctx.respond(embed=output, ephemeral = not viewable)

    @slash_command(name="alt")
    async def altname_slashglobal(self,ctx,viewable: discord.Option(bool) = True):

        output = await generate_alt(ctx)

        await ctx.respond(embed=output, ephemeral = not viewable)

def setup(bot):
    bot.add_cog(generate_alt_(bot))