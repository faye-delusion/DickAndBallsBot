import discord
from discord.ext import commands

import json
import datetime
import os
import asyncio
import random

# Create bot instance
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=">>", intents=intents)

config = {}

with open("config.json", "r") as file:

    config = json.load(file)

@bot.event
async def on_ready():

    # Empty out junk in console window
    clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clear()

    # Command Cog Handler
    print("Loading commands...")
    count = 1
    for file in os.listdir("Commands"):

        if file.endswith(".py"):

            filename = file[:-3]

            try:

                bot.load_extension(f"Commands.{filename}")

            except:

                print(f"Failed to load command {filename} ({count} / {len(os.listdir('Commands')) -1})")

            else:
                
                print(f"Loaded {filename} ({count} / {len(os.listdir('Commands')) -1})")

            count += 1

    print("Commands loaded, registering application commands... (This might take a minute)")
    await bot.register_commands()
    print("Application commands registered.")

    # Event Cog Handler
    print("Loading events...")
    count = 1
    for file in os.listdir("Events"):

        if file.endswith(".py"):

            filename = file[:-3]

            bot.load_extension(f"Events.{filename}")
            print(f"Loaded {filename} ({count} / {len(os.listdir('Events')) -1})")

            count += 1

    print("Events loaded.")

    await asyncio.sleep(0.3)
    clear()

    # Funny Print Stuff
    await asyncio.sleep(0.3)
    print("------------------------------------------------------------------------------------------------")
    await asyncio.sleep(0.3)
    print("""
██████╗░██╗░█████╗░██╗░░██╗  ░█████╗░███╗░░██╗██████╗░  ██████╗░░█████╗░██╗░░░░░██╗░░░░░░██████╗
██╔══██╗██║██╔══██╗██║░██╔╝  ██╔══██╗████╗░██║██╔══██╗  ██╔══██╗██╔══██╗██║░░░░░██║░░░░░██╔════╝
██║░░██║██║██║░░╚═╝█████═╝░  ███████║██╔██╗██║██║░░██║  ██████╦╝███████║██║░░░░░██║░░░░░╚█████╗░
██║░░██║██║██║░░██╗██╔═██╗░  ██╔══██║██║╚████║██║░░██║  ██╔══██╗██╔══██║██║░░░░░██║░░░░░░╚═══██╗
██████╔╝██║╚█████╔╝██║░╚██╗  ██║░░██║██║░╚███║██████╔╝  ██████╦╝██║░░██║███████╗███████╗██████╔╝
╚═════╝░╚═╝░╚════╝░╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░  ╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═════╝░
    """)
    await asyncio.sleep(0.3)
    print("------------------------------------------------------------------------------------------------")
    await asyncio.sleep(0.7)
    print(f"Written by: {config['author']['name']} ({config['author']['email']})")
    await asyncio.sleep(0.3)
    print(f"Last Restart: {datetime.datetime.utcfromtimestamp(config['last_restart']).strftime('%Y-%m-%d %H:%M:%S')} UTC")

    config["last_restart"] = datetime.datetime.now().timestamp()

    with open("config.json", "w") as file:

        json.dump(config, file, indent=4)

    await asyncio.sleep(0.3)

    splash_text = [

        "Welcome to the future, it looks like shit.",
        "Up Up Down Down Left Right B A Start",
        "print(\"Program Loaded\")",
        "If you're seeing this, where did your life go wrong?",
        "I can see my house from here!",
        "Something something jet fuel steel beams.",
        "Where did you sleep last night?",
        "So, what's your story then?",
        "Inspired by Minecraft.",
        "Coffee?",
        "F#!@",
        "Not a monkey JPG in sight...",
        "Did you hear that?",
        "^-^",
        "Trans Rights!",
        "Huh?",
        "Yep, this is real.",
        "Not a joke.",
        "Tim Apple would be proud.",
        "Enter cheat code:",
        "Deleting Sys32..."

    ]

    print(f"{random.choice(splash_text)}")


bot.run(config["token"])    