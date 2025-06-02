import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot_intents = discord.Intents.none()
bot_intents.message_content = True
bot_intents.guilds = True
bot_intents.guild_messages = True
bot_intents.members = True
# client = discord.Client(intents=bot_intents)
bot = commands.Bot(command_prefix='!', intents=bot_intents)

data = None
all_roles = None
t1 = None
t2 = None
bari = None
bass = None

# @client.event
@bot.event
async def on_ready():
    global data
    data = pd.read_excel("S Roster and Attendance - Spring 2025.xlsx",usecols=[0,1,3,5], index_col=2)
    data.index = data.index.str.lower()

    global all_roles
    all_roles = discord.utils.find(lambda g:g.name == "Bot Testing", bot.guilds).roles
    # all_roles = client.guilds[0].roles

    global t1
    global t2
    global bari
    global bass
    t1 = discord.utils.find(lambda r:r.name == "Tenor 1", all_roles)
    t2 = discord.utils.find(lambda r:r.name == "Tenor 2", all_roles)
    bari = discord.utils.find(lambda r:r.name == "Baritone", all_roles)
    bass = discord.utils.find(lambda r:r.name == "Bass", all_roles)

    print("Connected to the Guild!")
    

# @client.event
@bot.event
async def on_message(message: discord.Message):
    if message.guild.name != "Bot Testing": return
    
    if message.author == bot.user: return

    if message.content.startswith('!'): return


    # if message.channel.id != 1373362239532302399: return
    if message.channel.name == "verifications":
        normal_verify(message)
        return
    elif message.channel.name == "posted-announcements":
        post_announcement(message)
        return
    elif message.attachments != []:
        file_preview(message)
        return


    user = message.author
    email = message.content.lower()

    check = discord.utils.find(lambda r: r.name == "Nice Boi", all_roles)
    if check not in user.roles:
        if "@pitt.edu" not in email:
            email = f'{email}@pitt.edu'

        try:
            entry = data.loc[email]
            first = entry.get("First Name")
            last = entry.get("Last Name")
            section = entry.get("Voice Part").split(" (")[0]

            role = discord.utils.find(lambda r:r.name == section, all_roles)

            roles = user.roles

            await user.remove_roles(t1,t2,bari,bass,reason="Verification")

            await user.add_roles(check,role,reason="Verification")

            await user.edit(nick=f"{first} {last}")

            await message.reply("Verification completed! Welcome to the Glee Club! <:glee:1077812002107424879>")
        except:
            await message.reply("Sorry, that email wasn't found in my system. Please check for typos or wait a few days for admins to update the system.")


# @bot.command(name='verify', help="Verifies new members")
# @commands.has_guild_permissions(administrator=True)
# async def verify_normal(ctx : commands.Context, id: int, email : str):
#     print("Command run")

#     user = discord.utils.find(lambda u:u.id == id, ctx.guild.members)

#     if ctx.channel.id != 1373362239532302399: return
#     email = email.strip().lower()

#     check = discord.utils.find(lambda r: r.name == "Nice Boi", all_roles)
#     if check not in user.roles:
#         if not email.endswith('@pitt.edu'):
#             email = f'{email}@pitt.edu'

#         entry = data.loc[email]
#         # print("Found email")
#         first = entry.get("First Name")
#         # print("Found first name")
#         last = entry.get("Last Name")
#         # print("Found last name")
#         section = entry.get("Voice Part").split(" (")[0]
#         # print("Found voice part")

#         role = discord.utils.find(lambda r:r.name == section, all_roles)
#         print(f"Role type: {role}")

#         roles = user.roles

#         if (t1 in roles and t1 != role):
#             print("removing t1")
#             await user.remove_roles(t1,reason="Verification")
#         if (t2 in roles and t2 != role):
#             print("removing t2")
#             await user.remove_roles(t2,reason="Verification")
#         if (bari in roles and bari != role):
#             print("removing bari")
#             await user.remove_roles(bari,reason="Verification")
#         if (bass in roles and bass != role):
#             print("removing bass")
#             await user.remove_roles(bass,reason="Verification")

#         print("Adding roles")
#         await user.add_roles(check,role,reason="Verification")

#         print("editting nickname")
#         await user.edit(nick=f"{first} {last}")

#         await ctx.reply("Verification completed! Welcome to the Glee Club! <:glee:1077812002107424879>")
#         # try:
#         # except:
#         #     await ctx.reply("Sorry, that email wasn't found in my system. Please check for typos or wait a few days for admins to update the system.")

# @bot.event
# async def on_command_error(ctx, error : commands.CommandError):
#     if isinstance(error, commands.errors.CheckFailure):
#         await ctx.reply("Sorry, you don't have permission to run that command")
#     elif isinstance(error, commands.errors.TooManyArguments):
#         await ctx.reply("ERROR: Too many arguments; I don't know what to do with this")
#     elif isinstance(error, commands.errors.MissingRequiredArgument):
#         await ctx.reply(f"ERROR: Missing required argument `{error.param}`")
#     else:
#         await ctx.reply(f"{error}")

bot.run(TOKEN)