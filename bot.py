# Main Workflow
import discord
from discord import message
from discord import file
from discord.ext import commands
import os
from dotenv import load_dotenv
from datetime import datetime
from github import Github
import git
import pytz


# Custom classes
from helpers.emojis import Emojis

# Load/run nessesary components/functions
load_dotenv()

# Getting latest GitHub commit
g = Github(os.getenv("GITHUB_TOKEN"))
repo = g.get_repo("Mordai/PPKE-ITK-MI-2021-DCBot")
commits = repo.get_commits()
github_last_commit = commits[0]
github_messages = github_last_commit.commit.message.split('\n\n')
github_desc = "".join(github_messages[1:]) if len(github_messages[1:]) > 0 else "No desc given"

# Getting latest local git commit
try:
    local_repo = git.Repo(search_parent_directories=True)
    headcommit = local_repo.head.commit
    sha = local_repo.head.object.hexsha
    local_commiter = headcommit.committer.name
except:
    sha = ""
    local_commiter = ""

# General variables
tz = pytz.timezone('Europe/Budapest')
now = datetime.now(tz)


MAIN_SERVER_GUILD = os.getenv("ITK_SERVER_ID")
TOKEN = os.getenv("DC_TOKEN")

intents = discord.Intents.all()
intents.members = True

########## BOT content ##########
bot = commands.Bot(intents = intents)


# Default/main events
@bot.event
async def on_ready():
    print("Ready to go!")
    bot.CH_bot_log = bot.get_channel(891715602442510386)
    message_log_start = f"{Emojis.StatusEmojis.sparkle} `Bot started: " + now.strftime("%Y-%m-%d %H:%M:%S") + "`"
    try:
        message_local = "\n```Current HEAD → " + sha + \
        "\nCurrent author → " + local_commiter + "```"
    except:
        message_local = ""

    try:
        message_heroku = "\n```Current HEAD → " + os.getenv("HEROKU_SLUG_COMMIT") + \
        "\nCurrent author → HEROKU (deployment)" + \
        "\nCommit name: " + github_messages[0] + \
        "\nCommit desc: " + github_desc + "```"

    except:
        message_heroku = ""
        
    #await bot.CH_bot_log.send(message_log_start + message_local if os.getenv("HEROKU_DEPLOYMENT") == "NO" else message_log_start + message_heroku)

@bot.event 
async def on_member_join(member):
    role = member.guild.get_role(892034791321518151)
    print(role.name)
    await member.add_roles(role)

# Load extensions and run the BOT
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print('f{filename} added')

bot.run(TOKEN)