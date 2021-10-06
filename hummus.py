from sys import prefix

from requests.api import request
from discord.utils import get
from discord import message
from discord.enums import Theme
import discord, requests, json, os, shutil, subprocess, aiohttp, asyncio, sys, colorama, time, discum, random, datetime, ctypes
from discum.gateway.session import guild
from discord.ext.commands.core import command
from pypresence import Presence
from discord.ext.commands import CommandNotFound
from time import gmtime, sleep, strftime
from colorama import Fore, init
from discord.ext import commands    

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=37, cols=100))
init()
with open('Config.json') as f:
    config = json.load(f)
    token = config.get('token')
    prefix = config.get('prefix')
    rpctheme = config.get('rpctheme')
with open(f'./RPC/{rpctheme}.json') as f: 
    config = json.load(f)
    client_id = config.get('client_id')
    details = config.get('details')
    state = config.get('state')
    large_image = config.get('large_image')
    large_text = config.get('large_text')
    button1_text = config.get('button1_text')
    button2_text = config.get('button2_text')
    button1_url = config.get('button1_url')
    button2_url = config.get('button2_url')
os.system('cls')
colorama.init()
hummus = discord.Client()
hummus = commands.Bot(command_prefix=prefix, self_bot=True, case_insensitive=True, auto_reconnect=True)
hummus.remove_command('help')
start_time = time.time()
result = requests.get(f'https://canary.discord.com/api/v8/science', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
elapsed = time.time() - start_time
elapsed = '%.3f' % elapsed
client_id = f'{client_id}'
RPC = Presence(client_id)
RPC.connect()
RPC.update(
    details=f"{details}",
    state=f"{state}",

    large_image = f"final2",
    large_text=f"{large_text}",

    buttons = [
        {"label": f"{button1_text}", "url": f"{button1_url}"},
        {"label": f"{button2_text}", "url": f"{button2_url}"}
    ]
)


@hummus.event
async def on_ready():
    ctypes.windll.kernel32.SetConsoleTitleW("Hummus Client Moderation Selfbot")
    print(f"""{Fore.LIGHTYELLOW_EX}
$$\   $$\                                                           
$$ |  $$ |                                                          
$$ |  $$ |$$\   $$\ $$$$$$\$$$$\  $$$$$$\$$$$\  $$\   $$\  $$$$$$$\ 
$$$$$$$$ |$$ |  $$ |$$  _$$  _$$\ $$  _$$  _$$\ $$ |  $$ |$$  _____|
$$  __$$ |$$ |  $$ |$$ / $$ / $$ |$$ / $$ / $$ |$$ |  $$ |\$$$$$$\  
$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ | $$ | $$ |$$ |  $$ | \____$$\ 
$$ |  $$ |\$$$$$$  |$$ | $$ | $$ |$$ | $$ | $$ |\$$$$$$  |$$$$$$$  |
\__|  \__| \______/ \__| \__| \__|\__| \__| \__| \______/ \_______/ 
""")
    print(f'''
    {Fore.LIGHTYELLOW_EX}Account:   {Fore.WHITE}{hummus.user.name}#{hummus.user.discriminator} [{len(hummus.guilds)} Servers] [{len(hummus.user.friends)} Friends]
    {Fore.LIGHTYELLOW_EX}Ping:      {Fore.WHITE}{hummus.ws.latency * 1000:.4f}
    {Fore.LIGHTYELLOW_EX}RTheme:    {Fore.WHITE}{rpctheme}
    {Fore.LIGHTYELLOW_EX}Prefix:    {Fore.WHITE}{prefix}
{Fore.LIGHTYELLOW_EX}{'_' * 100}''')


@hummus.command()
async def furryspammer(ctx, amount: int):
    await ctx.message.delete()
    print(f'{Fore.WHITE}[{strftime("%H:%M", gmtime())}] | {Fore.LIGHTYELLOW_EX}[Command] {Fore.WHITE}| furryspammer | {amount} times')
    for i in range(amount):
        r = requests.get("https://sheri.bot/api/yiff/?format=json")
        res = r.json()
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
    if amount is None:
        await ctx.message.send('say a amount idot!!!!!!!!')
        asyncio.sleep(15)
        await ctx.message.delete()
    print(f'{Fore.WHITE}[{strftime("%H:%M", gmtime())}] | {Fore.LIGHTYELLOW_EX}[Command] {Fore.WHITE}| furryspammer | Finished')

@hummus.command()
@commands.guild_only()
async def massping(ctx, amount: int = 1):
    try:
        await ctx.message.delete()
        print(f'{Fore.WHITE}[{strftime("%H:%M", gmtime())}] | {Fore.LIGHTYELLOW_EX}[Command] {Fore.WHITE}| massping | {amount} times')
    except:
        pass
    DiscumClient = discum.Client(token=token, log=False)
    message = ""
    DiscumClient.gateway.fetchMembers(str(ctx.guild.id), str(ctx.channel.id))
    @DiscumClient.gateway.command
    def massmention(resp):
        if DiscumClient.gateway.finishedMemberFetching(str(ctx.guild.id)):
            DiscumClient.gateway.removeCommand(massmention)
            DiscumClient.gateway.close()
    DiscumClient.gateway.run()
    tosend = []
    for memberID in DiscumClient.gateway.session.guild(str(ctx.guild.id)).members:
        if len(message) < 1950:
            message += f"<@!{str(memberID)}>卍"
        else:
            tosend.append(message)
            message = ""
    tosend.append(message)
    for i in range(amount):
        for item in tosend:
            m = await ctx.send(item)
            try:
                await m.delete()
            except:
                print(f'[{strftime("%H:%M", gmtime())}] {Fore.WHITE}| {Fore.LIGHTYELLOW_EX} [Info] {Fore.WHITE}| Failed to delete message')
    
hummus.run(token, bot=False)