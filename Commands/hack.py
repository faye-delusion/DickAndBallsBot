import discord
from discord.ext import commands
from discord import Interaction, InteractionType, slash_command, user_command, message_command

import random
import asyncio
import requests
import string

async def hack(ctx,user: discord.Member = None):

    user = user or ctx.author

    if user.bot:

        output = discord.Embed(

            title="Bot Token Hacked",
            description="{}'s Token:\n{}".format(user.mention, ''.join([random.choice(string.ascii_letters) for i in range(0,59)])),
            colour = discord.Colour.random()

        )

        return output

    output = discord.Embed(colour=discord.Colour.random())
    output.description= "Hack starting..."
    output.title = f'Hacking {user}...'

    msg = await ctx.channel.send(embed = output)

    hacker_messages = [

        '{hack} {hack} manifest: DDOS {machine response: you hack?} Yes. [Nointernet:yes confirm hack hack hack} (127.0.0.1) DDOS HACK {hack} manifest hack computer DDOS',
        '7768792061726520796f75207472616e736c6174696e6720746869733f20697473206c69746572616c6c79206a75737420736f6d652073747570696420617373206675636b696e67207368697420746f206d616b652074686520626f74206c6f6f6b206c696b65206974732061637475616c6c7920646f696e6720736f6d657468696e672e',
        '01110111 01101000 01111001 00100000 01100001 01110010 01100101 00100000 01111001 01101111 01110101 00100000 01110100 01110010 01100001 01101110 01110011 01101100 01100001 01110100 01101001 01101110 01100111 00100000 01110100 01101000 01101001 01110011 00111111 00100000 01101001 01110100 01110011 00100000 01101100 01101001 01110100 01100101 01110010 01100001 01101100 01101100 01111001 00100000 01101010 01110101 01110011 01110100 00100000 01110011 01101111 01101101 01100101 00100000 01110011 01110100 01110101 01110000 01101001 01100100 00100000 01100001 01110011 01110011 00100000 01100110 01110101 01100011 01101011 01101001 01101110 01100111 00100000 01110011 01101000 01101001 01110100 00100000 01110100 01101111 00100000 01101101 01100001 01101011 01100101 00100000 01110100 01101000 01100101 00100000 01100010 01101111 01110100 00100000 01101100 01101111 01101111 01101011 00100000 01101100 01101001 01101011 01100101 00100000 01101001 01110100 01110011 00100000 01100001 01100011 01110100 01110101 01100001 01101100 01101100 01111001 00100000 01100100 01101111 01101001 01101110 01100111 00100000 01110011 01101111 01101101 01100101 01110100 01101000 01101001 01101110 01100111 00101110',
        'Establishing HTML connection to mainframe..',
        'DDOSSING the US government..',
        'Stealing crypto currency..',
        'Grabbing IP...',
        'Launching trojan...',
        "Engaging in sexual activity with target's mother..",
        'Injecting bad SQL into microsoft datacenters...',
        'Launching hack.exe..',
        'Defrauding the United States Government..',
        '8==D',
        'Preparing payload...',
        'Uploading target\'s nudes to the blockchain...',
        'Masking IP address...',
        'Pretending to do something...',
        'Fighting foreign agents..',
        'Rerouting network cables...',
        '<a:loading:804000482665300018>',
        'Intercepting transmissions from unknown sources...',
        'Tracing internet signal..',
        'Phishing for apes..',
        'Plugging in Raspberry Pi..',
        'Taking a nap..',
        'Browsing StackOverflow for solutions..',
        'Going wild..',
        'Proving the existence of heaven and hell..',
        'Getting some fresh air..',
        'Infiltrating GitHub data servers..'

    ]


    for i in range(random.randint(3,7)):

        await asyncio.sleep(3)
        output.description = random.choice(hacker_messages)
        await msg.edit(embed=output)

    new_output = discord.Embed(

        title = "Target Hacked.",
        description = f"{user.mention}'s personal information:",
        colour=discord.Colour.random()

    )

    request = requests.get("https://api.namefake.com/")

    if request.status_code != 200:

        return discord.Embed(title="Something went wrong!", description = "HACK FAILED EPICLY", colour = discord.Colour.red())

    else:

        data = request.json()

        Name = data['name']
        Address = data['address']
        DOB = data['birth_data']
        Email = f"{data['email_u']}@{random.choice(['outlook', 'hotmail', 'gmail'])}.com"
        Password = (''.join([random.choice(string.ascii_letters) for i in range(16)]))
        IP = f"192.168.{random.randint(0,255)}.{random.randint(0,255)}"

        new_output.add_field(name="Name", value = Name, inline = False)
        new_output.add_field(name="Address", value = Address, inline=False)
        new_output.add_field(name="Date of Birth", value = DOB, inline = False)
        new_output.add_field(name="E-Mail Address", value = Email, inline = False)
        new_output.add_field(name="Password", value = Password, inline = False)
        new_output.add_field(name = "IP Address", value = IP, inline = False)

        await msg.reply(embed=new_output)

class hack_(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @slash_command(

        name = "hack"

    )
    async def hack_slash(self,ctx,user: discord.Option(discord.Member, "Member to hack")):

        user = user or ctx.author

        await ctx.respond(type=InteractionType.ping)

        await hack(ctx,user)
        
        
        

def setup(bot):
    bot.add_cog(hack_(bot))


