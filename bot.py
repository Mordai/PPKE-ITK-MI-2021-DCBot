#Main Workflow

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from datetime import datetime
import subprocess
import pytz


#Custom classes
import emojis

#Load/run nessesary components/functions
load_dotenv()

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
        message_local = "\n```Current HEAD → " + subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip() + \
        "\nCurrent author → " + subprocess.check_output(['git', 'config', '--global', 'user.name']).decode('UTF-8') + "```"
    except:
        message_local = ""

    try:
        message_heroku = "\n```Current HEAD → " + os.getenv("HEROKU_SLUG_COMMIT") + \
        "\nCurrent author → HEROKU deployment" + \
        "\nCommit desc → " + os.getenv("HEROKU_SLUG_DESCRIPTION")
    except:
        message_heroku = ""


    await bot.CH_bot_log.send(message_log_start + message_local if os.getenv("HEROKU_DEPLOYMENT") == "NO" else message_log_start + message_heroku)


bot.run(TOKEN)