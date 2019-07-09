import discord
from discord.permissions import *
from .localsettings import *

client = discord.Client()

@client.event
async def on_ready():
    print('The bot is ready')
    await client.change_presence(activity=discord.Game(name="Making a bot"))
    Guild = client.get_guild(593004137495527426)
    print(Guild.roles)
    parent = Guild.get_role(593004137495527426)
    await Guild.create_role(name="test",permissions=parent.permissions)
    y = ''
    for x in client.get_all_members():
        z = x.nick
        
        z = str(z).split(' |')[0]
        try:
            print(int(z))
            s = await Guild.create_role(name=z,permissions=parent.permissions)
            await x.add_roles(s)
        except:
            print('not a number')
        y+=str(z)+'\n'
    print(y)

    
    print(x.name)
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        y = ''
        for x in client.get_all_members():
            z = x.nick
            print(z)
            z = str(z).split(' |')[0]
            y+=str(z)+'\n'
        await message.channel.send(y)
client.run(TOKEN)