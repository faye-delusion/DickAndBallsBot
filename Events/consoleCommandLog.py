import discord
from discord.ext import commands

import datetime

def get_time_formatted():

    time = datetime.datetime.now().strftime("[%H:%M:%S]")

    return time
class commandLog(commands.Cog):

    def __init__(self,bot):

        self.bot = bot

    @commands.Cog.listener(name="on_command_completion")
    async def command_complete(self,command):

        print(f"{command.name} command {dir(command)}")

    @commands.Cog.listener(name="on_application_command_completion")
    async def application_command_complete(self,command):

        print(f"{get_time_formatted()} {command} command executed.")

def setup(bot):

    bot.add_cog(commandLog(bot))