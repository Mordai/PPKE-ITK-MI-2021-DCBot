#Main Workflow

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from datetime import datetime
import subprocess
import getpass


#Custom classes
import emojis

#Load/run nessesary components/functions
load_dotenv()

 #General variables
now = datetime.now()
MAIN_SERVER_GUILD = os.getenv("ITK_SERVER_ID")
TOKEN = os.getenv("DC_TOKEN")

bot = discord.Bot()

@bot.event
async def on_ready():
    print("Ready to go!")
    bot.CH_bot_log = bot.get_channel(891715602442510386)
    await bot.CH_bot_log.send(f"{emojis.Emojis.StatusEmojis.sparkle} `Bot started: " + now.strftime("%Y-%m-%d %H:%M:%S") + "`"\
    "\n```Current HEAD → " + subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip() + \
    "\nCurrent author → " + subprocess.check_output(['git', 'config', '--global', 'user.name']).decode('UTF-8') + "```" if os.getenv("RUN_ON_HEROKU") == "NO" else "HEROKU deployment" + "```")


bot.run(TOKEN)