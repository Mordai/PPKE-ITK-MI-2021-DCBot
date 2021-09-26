#Main Workflow

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from datetime import datetime
import subprocess
from github import Github
import git
import pytz


#Custom classes
import emojis

#Load/run nessesary components/functions
load_dotenv()
g = Github(os.getenv("GITHUB_TOKEN"))
repo = g.get_repo("Mordai/PPKE-ITK-MI-2021-DCBot")
commits = repo.get_commits()
last_commit = commits[0]
messages = last_commit.commit.message.split('\n\n')
print(messages[0])
print("\n".join(messages[1:]))

try:
    local_repo = git.Repo(search_parent_directories=True)
    sha = local_repo.head.object.hexsha
except:
    sha = ""

#General variables
tz = pytz.timezone('Europe/Budapest')
now = datetime.now(tz)


MAIN_SERVER_GUILD = os.getenv("ITK_SERVER_ID")
TOKEN = os.getenv("DC_TOKEN")

bot = discord.Bot()


@bot.event
async def on_ready():
    print("Ready to go!")
    bot.CH_bot_log = bot.get_channel(891715602442510386)
    message_log_start = f"{emojis.Emojis.StatusEmojis.sparkle} `Bot started: " + now.strftime("%Y-%m-%d %H:%M:%S") + "`"
    try:
        message_local = "\n```Current HEAD → " + sha + \
        "\nCurrent author → " + subprocess.check_output(['git', 'config', '--global', 'user.name']).decode('UTF-8') + "```"
    except:
        message_local = ""

    try:
        message_heroku = "\n```Current HEAD → " + os.getenv("HEROKU_SLUG_COMMIT") + \
        "\nCurrent author → HEROKU deployment" + \
        "\nCommit name → " + last_commit.commit.message.split('\n\n')[0] + \
        "\nCommit desc → "  + last_commit.commit.message.split('\n\n')[1:] + \
        "\nHeroku slug desc → " + os.getenv("HEROKU_SLUG_DESCRIPTION") + "```"

    except:
        message_heroku = ""

    #message_log_start + message_local if os.getenv("HEROKU_DEPLOYMENT") == "NO" else 
    await bot.CH_bot_log.send(message_log_start + message_heroku)


#bot.run(TOKEN)