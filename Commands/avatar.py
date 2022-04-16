import discord
from discord import slash_command
from discord.ext import commands

import json

with open("config.json", "r") as f:

    config = json.load(f)

guilds = config["test_guilds"]

async def avatar(ctx, user):

    embed = discord.Embed(

        title=f"{user.name}'s Avatar",
        colour=discord.Colour.random()

    )

    embed.set_image(url=user.avatar.url)

    return embed

class avatar_(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="avatar")
    async def avatar_chat(self,ctx,user: discord.Member = None):

        user = user or ctx.author

        output = await avatar(ctx, user)

        await ctx.reply(embed=output)

    @slash_command(name="avatar", guild_ids=guilds)
    async def avatar_slash(self,ctx, user: discord.Option(discord.Member) = None, viewable: discord.Option(bool) = True):

        user = user or ctx.author

        output = await avatar(ctx, user)

        await ctx.respond(embed=output, ephemeral = not viewable)

    @slash_command(name="avatar")
    async def avatar_slashglobal(self,ctx,user: discord.Option(discord.Member) = None, viewable: discord.Option(bool) = True):

        user = user or ctx.author

        output = await avatar(ctx,user)

        await ctx.respond(embed=output, ephemeral = not viewable)

def setup(bot):

    bot.add_cog(avatar_(bot))