import discord
from discord import slash_command, message_command
from discord.ext import commands

import json

with open("config.json", "r") as f:

    config = json.load(f)

guilds = config["test_guilds"]

async def poll(ctx,subject: str):

    embed = discord.Embed(

        title="Poll:",
        description=subject,
        colour=discord.Colour.random()

    )

    m = await ctx.send(embed=embed)

    for reaction in ["👍", "👎"]:

        await m.add_reaction(reaction)

class poll_(commands.Cog):

    def __init__(self,bot):

        self.bot = bot

    @commands.command(name="poll")
    async def poll_chat(self,ctx,*, subject: str):

        await poll(ctx, subject)

    @slash_command(name="poll", guild_ids=guilds)
    async def poll_slash(self,ctx,subject: str):

        await poll(ctx,subject)

        await ctx.respond("Poll started 🙂", ephemeral=True)

    @message_command(name="Run as Poll", guild_ids=guilds)
    async def poll_message(self,ctx,message: discord.Message):

        subject = message.content

        await poll(ctx, subject)

        await ctx.respond("Poll started 🙂", ephemeral=True)
        
def setup(bot):

    bot.add_cog(poll_(bot))