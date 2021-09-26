#Main Workflow

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from datetime import datetime

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
    bot.CH_bot_log.send(f"Bot started: ", now.strftime("%Y-%m-%d %H:%M:%S"))


bot.run(TOKEN)