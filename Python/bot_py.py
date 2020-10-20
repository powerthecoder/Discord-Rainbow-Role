import os
import sys
import asyncio
try:
    import json
    import random
    import discord
    from discord.ext import commands, tasks
    from discord.utils import get
except:
    os.system("python3 -m pip install -U discord.py")
    os.system("python3 -m pip install -U discord.py[voice]")
    os.system("python3 -m pip install -U random")
    os.system("python3 -m pip install -U json")

Token = input("Token: ")
Role_Name = input("Role Name: ")

client = commands.Bot(command_prefix="&")

@client.event
async def on_ready():
    print("""

------------------------------------------------------------------------
Developer: Leo Power
GitHub: https://github.com/powerthecoder
Website: https://powerthecoder.xyz/

Disclaimer:
This program can get your Discord account terminated and should
be used at your own risk. Anything that you do or happens to you
is not the developer Leo Power's fault. This was made for educational
purposes only!
------------------------------------------------------------------------
type &start in Discord to start the rainbow role

    """)

@client.command()
async def start(ctx):
    global Role_Name
    colours = [0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff, 0xff0053]
    role = discord.utils.get(ctx.guild.roles, name=Role_Name)
    x = 0
    while (x != 1):
        #await ctx.guild.edit_role(role=role, color=random.choice(colours))
        await role.edit(colour=random.choice(colours))
        await asyncio.sleep(5)



client.run(Token)
