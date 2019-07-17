import discord
from discord.ext import commands
from discord.permissions import *
from localsettings import *
from util import *

client = commands.Bot(command_prefix='.')



@client.event
async def on_ready():
    print('The bot is ready')



@client.command()
async def ping(ctx):
    
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')


@client.command()
async def arrange(ctx):
    await ctx.send(f'Hey {ctx.author},\n`I wil help you with that.`\n `Following are list of roles which are being created and assigned`')
    newly_created = set()
    newly_assigned = set()
    for member in client.get_all_members():
        print('nick name',member.nick)
        try:
            role  = classify(member.nick)
        except:
            continue
        """Code for creating new roles or assigning existing roles"""        
        
        searched_role = discord.utils.get(ctx.guild.roles,name='Team-'+role)
        print('Found an exising role : ', searched_role)
        if  searched_role!= None:
            await member.add_roles(searched_role,reason=None)
            newly_assigned.add(searched_role.name)
        else:
            print('Creating new role : Team-',role)
            if is_role_int(role):
                new_role = await ctx.guild.create_role(name='Team-'+role,hoist=True,reason='maintainance')
                await member.add_roles(new_role,reason=None)
                newly_created.add(new_role.name)
    await ctx.send(f'`{len(newly_created)} roles were created as follows : `')
    for role in newly_created:
        await ctx.send(f'\t`{role}`')
    await ctx.send(f'`{len(newly_assigned)} roles were assigned as follows : `')
    for role in newly_assigned:
        await ctx.send(f'\t`{role}`')


        """Code for creating channel category"""
    await ctx.send('`Roles have been successfullly assigne`\n`Please user` mentoring `command to assign mentors`')
        


    """Code for creating text channels based on roles"""
        #channel = await ctx.guild.create_text_channel('cool-channel')

    
    # if message.author == client.user:
    #     return

    # if message.content.startswith('$'):
    #     if message.content == '$arrange':
    #         await message.channel.send('`I will help you`')
    #         for user in client.get_all_members():
    #             role = get_role_name(user)
    #             if is_role_int:main
    #                 try:
    #                     new_role = create_role(Guild,role,PERM)
    #                 except Exception as e:
    #                     print(str(e))
    #                     new_role = get_role_by_name(Guild,role)
    #                 await user.add_roles(new_role)
    #     if message.content == '$':
    #         await message.channel.send('Help Menu')

client.run(TOKEN)