import discord
from discord import slash_command, user_command, message_command

from discord.ext import commands

import json

with open("config.json", "r") as f:

    config = json.load(f)

guilds = config["test_guilds"]

async def whois(ctx, user: discord.Member):

    profile_badges = []

    # Hypesquad
    profile_badges.append("<:hype_balance_badge:939744472084906025>") if user.public_flags.hypesquad_balance else None
    profile_badges.append("<:hype_bravery_badge:939744472005218374>") if user.public_flags.hypesquad_bravery else None
    profile_badges.append("<:hype_brilliance_badge:939744472026185798>") if user.public_flags.hypesquad_brilliance else None

    # Early Supporter
    profile_badges.append("<:early_supporter_badge:939744472214937650>") if user.public_flags.early_supporter else None

    # Partner
    profile_badges.append("<:partner_badge:939744472139431968>") if user.public_flags.partner else None

    # Moderator
    profile_badges.append("<:moderator_badge:939750553095929957>") if user.public_flags.discord_certified_moderator else None

    # Bot Developer
    profile_badges.append("<:bot_dev_badge:939751762091442176>") if user.public_flags.verified_bot_developer else None

    embed = discord.Embed(

        title = f"{user}",
        description="{}".format(' '.join(profile_badges)),
        colour=discord.Colour.random()

    )

    embed.add_field(

        name = "ID",
        value=f"{user.id}"

    )

    embed.add_field(

        name = "Account Creation Date",
        value = f"<t:{int(user.created_at.timestamp())}> (<t:{int(user.created_at.timestamp())}:R>)"

    )

    embed.add_field(

        name = "Joined",
        value=f"<t:{int(user.joined_at.timestamp())}> (<t:{int(user.joined_at.timestamp())}:R>)"

    )

    if not user.avatar:

        embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")

    else:

        embed.set_thumbnail(url=user.avatar.url)

    return embed

class whois_(commands.Cog):

    def __init__(self, bot):

        self.bot = bot


    @commands.command(name = "whois")
    async def whois_chat(self,ctx,user: discord.Member = None):

        user = user or ctx.author

        output = await whois(ctx, user)

        await ctx.reply(embed=output)

    @slash_command(name = "whois", guild_ids = guilds)
    async def whois_slash(self, ctx, user: discord.Option(discord.User) = None, viewable: discord.Option(bool) = True):

        user = user or ctx.author

        output = await whois(ctx, user)

        await ctx.respond(embed=output, ephemeral = not viewable)

    @slash_command(name = "whois")
    async def whois_slashglobal(self, ctx, user: discord.Option(discord.User) = None, viewable: discord.Option(bool) = True):

        user = user or ctx.author

        output = await whois(ctx, user)

        await ctx.respond(embed=output, ephemeral = not viewable)

    @user_command(name = "Who is", guild_ids=guilds)
    async def whois_user(self,ctx,user: discord.User):

        output = await whois(ctx,user)

        await ctx.respond(embed = output, ephemeral = True)

    @user_command(name = "Who is")
    async def whois_userglobal(self,ctx,user: discord.User):

        output = await whois(ctx,user)

        await ctx.respond(embed = output, ephemeral = True)

    @message_command(name="Who is", guild_ids=guilds)
    async def whois_message(self,ctx,message:discord.Message):

        user = message.author

        output = await whois(ctx, user)

        await ctx.respond(embed=output, ephemeral = True)

    @message_command(name="Who is")
    async def whois_messageglobal(self,ctx,message:discord.Message):

        user = message.author

        output = await whois(ctx, user)

        await ctx.respond(embed=output, ephemeral = True)

def setup(bot):

    bot.add_cog(whois_(bot))