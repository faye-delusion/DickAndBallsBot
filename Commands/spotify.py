import discord
from discord import slash_command, message_command, user_command
from discord.ext import commands

import datetime
import time
import json
with open("config.json", "r") as f:

    config = json.load(f)

guilds = config["test_guilds"]

async def spotify(ctx,user, spotify):

    embed = discord.Embed(

        title=f"{spotify.title}",
        colour=spotify.color

    )

    embed.set_image(url=spotify.album_cover_url)

    embed.add_field(

        name="Listen on Spotify",
        value=f"[Listen Here]({spotify.track_url})"

    )

    duration = spotify.duration.total_seconds()
    duration = time.gmtime(duration)
    duration = time.strftime("%M:%S", duration)

    embed.add_field(

        name="Duration",
        value=duration

    )

    embed.add_field(

        name="Album",
        value=f"{spotify.album}"

    )

    embed.add_field(

        name="Artist(s)",
        value="{}".format(', '.join(spotify.artists))

    )

    return embed

class spotify_(commands.Cog):

    def __init__(self,bot):

        self.bot = bot

    @commands.command(name="spotify")
    async def spotify_chat(self,ctx,user: discord.Member = None):

        user = user or ctx.author

        for activity in user.activities:

            if type(activity) == discord.Spotify:

                output = await spotify(ctx,user,activity)

                return await ctx.reply(embed=output)

        await ctx.reply(embed=discord.Embed(title=f"{user.name} is not listening to anything at the moment.", colour=discord.Colour.random()))

    @slash_command(name="spotify", guild_ids=guilds)
    async def spotify_slash(self,ctx,user: discord.Option(discord.Member) = None, viewable: discord.Option(bool) = True):

        user = user or ctx.guild.get_member(ctx.author.id)

        for activity in user.activities:

            if type(activity) == discord.Spotify:

                output = await spotify(ctx,user,activity)

                return await ctx.respond(embed=output, ephemeral = not viewable)

        await ctx.respond(embed=discord.Embed(title=f"{user.name} is not listening to anything at the moment.", colour=discord.Colour.random()))

    @slash_command(name="spotify")
    async def spotify_slashglobal(self,ctx,user: discord.Option(discord.Member) = None, viewable = False):

        user = user or ctx.guild.get_member(ctx.author.id)

        for activity in user.activites:

            if type(activity) == discord.Spotify:

                output = await spotify(ctx,user,activity)

                return await ctx.respond(embed = output, ephemeral = not viewable)



def setup(bot):

    bot.add_cog(spotify_(bot))