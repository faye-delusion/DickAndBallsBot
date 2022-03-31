import discord
from discord.ext import commands

class commandLog(commands.Cog):

    def __init__(self,bot):

        self.bot = bot

    @commands.Cog.listener(name="on_command_completion")
    async def command_complete(self,command):

        print(f"{command.name} command {dir(command)}")

def setup(bot):

    bot.add_cog(commandLog(bot))