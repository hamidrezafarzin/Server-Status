"""

    Server Status FiveM Bot

    Developed By : H_VICTOR#2999

    Read the descriptions and comments to change the codes and values.
    License :
    
    GNU General Public License v3.0 Li
    http://www.gnu.org/licenses/

"""
import asyncio
import json
import requests
from requests import get
import colorama
import discord
from discord.ext import commands, tasks



# Read The Config And Get Token Discord Bot From Config.json
with open('config.json', 'r') as file:
    config = json.load(file)
    TOKEN = config["TOKEN"]
    IP = config["Server_ip"]

def create_data():
    """
    If the config file is deleted, this file will be re-created with the help of this function and the steps will be completed.
    The bot token is held and there is no need to reset it.

    NOTE : Please do not change the color filters list.
    Changing this list will cause problems with the bot.
    """

    base_config = {
    "TOKEN": TOKEN,
    "prefix": "H!",
    "Server_ip": IP,
    "Channel_id": None,
    "Message_id": None,
    "color_filter": ["^0", "^1", "^2", "^3", "^4", "^5", "^6", "^7", "^8", "^9"]
    }
    # Save Data
    with open ("config.json", 'w') as file :
        json.dump(base_config, file, indent=2)



colorama.init()
intents = discord.Intents.all()
# If you use all intentions, delete the following two variables.
intents.presences = False
intents.members = False
# --------------------
bot = commands.Bot(command_prefix = config["prefix"], help_command=None, intents=intents)

@bot.event
async def on_ready():
    """
    This function is executed when the bot is fully executed and ready to work.
    """
    print(f"""\u001b[32m{bot.user.name} is ready """)
    print('\u001b[32mDev : \u001b[37mH_VICTOR#2999')

@bot.command()
async def ping(ctx):
    await ctx.send(f"**Bot ping : {round(bot.latency * 1000)}ms**")

@commands.guild_only()
@bot.command()
async def set_status(ctx, *, Channel : discord.TextChannel = None):
    """
    This command sends the information and shows the status of the server.
    This command receives and stores a text channel and checks that a configured server is present and free from malfunction, and then does its job.
    """
    authorperms = ctx.author.guild_permissions
    if authorperms.administrator:
        if Channel != None :
            try :
                with open ('config.json', 'r') as file :
                    data = json.load(file)
            except FileNotFoundError:
                # if not found config file  , re-created config file
                create_data()
                await asyncio.sleep(2)
            ip = data["Server_ip"]
            Get_dynamic = get(f'http://{ip}/dynamic.json', timeout=5)
            Get_players = get(f'http://{ip}/players.json', timeout=5)
            if ip == None or ip == "" :
                await ctx.send("Please enter the IP in the config.json file")
                print("\u001b[33mPlease enter the IP in the config.json file")
            elif Get_dynamic.status_code == 200 or Get_players.status_code == 200 :
                await ctx.send("ok i find out the server")
                data["Channel_id"] = Channel.id
                Get_dynamic = Get_dynamic.json()
                Get_players = Get_players.json()
                Host_name = Get_dynamic["hostname"]
                # FiveM colored words are filtered here so that they are not displayed
                for i in data["color_filter"] :
                    if i in Host_name :
                        Host_name = Host_name.replace(i, "")
                embed=discord.Embed(color=0x404EED)
                embed.description = "**Players: " + str(Get_dynamic["clients"]) + "/" + str(Get_dynamic["sv_maxclients"]) +"**\n"
                embed.set_author(name=Host_name)
                
                for x in Get_players:
                    embed.description += f"\n" + "> " + "[" + str(x["id"]) + "] " + "`" + str(x["name"]) + "`"
                embed.set_footer(text="Developed By H_VICTOR#2999 | Updated automatically every 15 seconds")
                msg = await Channel.send(embed=embed)
                data["Message_id"] = msg.id
                with open ("config.json", 'w') as file :
                    json.dump(data, file, indent=2)
            elif Get_dynamic.status_code != 200 or Get_players.status_code != 200 :
                await ctx.send("The server is offline Please check again when the server is online or check the IP address")
                print("\u001b[33mThe server is offline Please check again when the server is online or check the IP address")
            
    else:
        msg = await ctx.send(f"{ctx.message.author} You Do Not have permission To Use This Command")
        await asyncio.sleep(5)
        try:
            await msg.delete()
        except Exception:
            pass

# For Calculating Count Of Users IP Server
Old_Players = -1
@tasks.loop(seconds = 15)
async def Check_players():
    # bot until ready : To avoid any problems using this function, we will make sure that the bot is fully set up to start checking the IP server.
    await bot.wait_until_ready()
    global Old_Players
    try :
        with open ("config.json", 'r') as file :
            data = json.load(file)
    except FileNotFoundError:
        create_data()
        await asyncio.sleep(2)
    ip = data["Server_ip"]
    if ip != None :
        # If the IP is set, the bot will check and try to connect to the server, and if all goes well, the message sent by the bot will be edited.
        if data["Channel_id"] and data["Message_id"] != None:
            try :
                Get_dynamic = get(f'http://{ip}/dynamic.json', timeout=5)
                Get_players = get(f'http://{ip}/players.json', timeout=5)
                if Get_dynamic.status_code == 200 or Get_players.status_code == 200 :
                    Get_dynamic = Get_dynamic.json()
                    Get_players = Get_players.json()
                    Host_name = Get_dynamic["hostname"]
                    for i in data["color_filter"] :
                        if i in Host_name :
                            Host_name = Host_name.replace(i, "")
                    embed=discord.Embed(color=0x404EED)
                    embed.description = "**Players: " + str(Get_dynamic["clients"]) + "/" + str(Get_dynamic["sv_maxclients"]) +"**\n"
                    embed.set_author(name=Host_name)
                    for x in Get_players:
                        embed.description += f"\n" + "> " + "[" + str(x["id"]) + "] " + "`" + str(x["name"]) + "`"
                    embed.set_footer(text="Developed By H_VICTOR#2999 | Updated automatically every 15 seconds")
                    try:
                        channel = bot.get_channel(data["Channel_id"])
                        msg = await channel.fetch_message(data["Message_id"])
                        await msg.edit(embed=embed)
                    except Exception:
                        print("\u001b[33mMessage not editable, please use the set_status command")
                        create_data()
                if Get_dynamic["clients"] == Old_Players:
                    pass
                elif Get_dynamic["clients"] != Old_Players:
                    Old_Players = Get_dynamic["clients"]
                    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= "Players: " + str(Get_dynamic["clients"]) + "/" + str(Get_dynamic["sv_maxclients"])))
            
            except Exception :
                # If for any reason the robot can not connect to the server, the text of the server unavailability is displayed in the status bot.
                channel = bot.get_channel(data["Channel_id"])
                msg = await channel.fetch_message(data["Message_id"])
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="🔴Server is unavailable🔴"))
                embed=discord.Embed(color=0xe40000)
                embed.description = "🔴Server is unavailable🔴"
                embed.set_footer(text="Developed By H_VICTOR#2999 | Updated automatically every 15 seconds")
                try:
                    await msg.edit(embed=embed)
                except Exception:
                    # If the message sent by the bot is deleted, the information will return to the previous state so that the robot can continue working.
                    print("\u001b[33mMessage not editable, please use the set_status command")
                    create_data()
                print("\u001b[33mFaild to Fetch server Player pls check your ip in config.json or start your server")
    elif ip == None :
        # If the IP is not set, it will be executed
        if data["Channel_id"] and data["Message_id"] != None:
            channel = bot.get_channel(data["Channel_id"])
            msg = await channel.fetch_message(data["Message_id"])
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="pls set ip and port in config.json !"))
            embed=discord.Embed(color=0xe40000)
            embed.description = "pls set ip and port in config.json !"
            embed.set_footer(text="Developed By H_VICTOR#2999 | Updated automatically every 15 seconds")
            try:
                await msg.edit(embed=embed)
            except Exception:
                print("\u001b[33mMessage not editable, please use the set_status command")
                create_data()

# Task Created , Every 15 Secound Runned.
Check_players.start()

# Start Bot
bot.run(TOKEN, reconnect=True)
