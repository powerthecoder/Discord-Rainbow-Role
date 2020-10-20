import os
import sys

try:
    import json
    import random
    import discord
    from discord.ext import commands
except:
    os.system("python3 -m pip install -U discord.py")
    os.system("python3 -m pip install -U discord.py[voice]")
    os.system("python3 -m pip install -U random")
    os.system("python3 -m pip install -U json")

with open(os.path.join(sys.path[0], "config.json"), "r") as f:
    data = json.load(f)
Token = input("Token: ")
Role_Name = input("Role Name: ")
Server_ID = int(input("Server ID: "))
data['Token'] = Token
data['Role_Name'] = Role_Name
data['Server_ID'] = int(Server_ID)
with open(os.path.join(sys.path[0], "config.json"), "w") as f:
    json.dump(data, f)

client = commands.Bot(command_prefix=">")

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

    """)


@client.event
async def rainbow_role():
    await client.wait_until_ready()
    global Role_Name
    global Server_ID
    colors = []
    server = await on_ready
    while not client.is_closd():
        await client.edit_role(server=Server_ID, role=role_Name, colour=discord.Colour(random.choice(colors)))
        await asyncio.sleep(5)

client.run(Token)
