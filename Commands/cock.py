import discord
from discord.ext import commands
from discord import slash_command

import random

async def cock(ctx, bot, user: discord.Member = None):

    user = user or ctx.author

    length_category = random.randint(0,10)

    cock_length = 0
    comment = ""

    if length_category <= 4:

        cock_length = random.randint(0,4)
        comments = [

            "PAHAHAHAHAHAHA",
            "it's fucking tiny!",
            "it's alright, maybe it'll grow one day..",
            "uhhhhh",
            "shitttt",
            "LOL",
            "it could be worse, i guess."

        ]

        comment = random.choice(comments)

    elif length_category > 4 and length_category <= 8:

        cock_length = random.randint(5,9)
        comments = [

            "Alright.",
            "cool",
            "sick",
            "getting somewhere",
            "awesome"

        ]

        comment = random.choice(comments)

    else:

        cock_length = random.randint(10,12)
        comments = [

            "HOLY",
            "GOD DAMN",
            "SHEEEESH",
            "HOLY SHIT",
            "WOAH"

        ]

        comment = random.choice(comments)

    output = discord.Embed(

        title = "COCK RATING",
        description = f"{user.mention}, you have a **{cock_length}** inch cock!",
        colour=discord.Colour.random()

    )

    output.add_field(

        name = "\u2800",
        value = "**8{}D**".format(''.join(['=' for i in range(0,cock_length)])),
        inline = True

    )

    output.set_footer(text=comment)

    return output

class cock_(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @slash_command(

        name="cock"

    )
    async def cock_slash(self,ctx,user: discord.Option(discord.Member) = None):

        user = user or ctx.author

        output = await cock(ctx,self.bot,user)

        await ctx.respond(embed=output, ephemeral = False)

    @commands.command(name = "cock")
    async def cock_chat(self,ctx,user: discord.Member = None):

        user = user or ctx.author

        output = await cock(ctx, self.bot, user)

        await ctx.reply(embed = output)

def setup(bot):
    bot.add_cog(cock_(bot))

    