import discord
from discord.ext import commands
from config import settings
import json
import requests



client = commands.Bot(command_prefix = settings["prefix"])                   

@client.event
async def on_ready():
    print(f"bruh ...(that s mean i am ready mr Abdul) ")

@client.event
async def on_member_join(member):
    print(f'صيداتي صادتي الصاعوديين رحبوا معي ب {member}')
    
@client.event
async def on_member_remove(member):
    print(f'ريح للسد لا نحتاج اصحاب العقول في مخططتنا اصلا {member}')

@client.command(aliases=['5ree','free'])
async def pong(ctx,* ,message:str):
    msg=ctx.message.content
    if message =='5ire' or message =='fire' or msg =='.pong':
        if (client.latency * 1000) < 100:
            ping_msg = "5ree 5ire hhhh ..lol ..kan el ping tale3 rahou min topnet howwa "
        else:
            ping_msg = "5ire 5ire :( Internet is so slow and I am sadge"
        await ctx.send(f'{ping_msg} {round(client.latency *1000)}ms')
@client.command()
async def ping(ctx):
    msg=ctx.message.content
    if msg =='.ping':
        if (client.latency * 1000) < 100:
            ping_msg = "5ree 5ire hhhh ..lol ..kan el ping tale3 rahou min topnet howwa "
        else:
            ping_msg = "5ire 5ire :( Internet is so slow and I am sadge"
        await ctx.send(f'{ping_msg} {round(client.latency *1000)}ms')
    
@client.command(aliases=['3awed'])
async def repeat(ctx, *, message:str):
    await ctx.send(message)
    print(message)
    


    
client.run(settings["token"]).print
