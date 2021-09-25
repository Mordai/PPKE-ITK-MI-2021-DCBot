#Main Workflow

import discord
from discord.ext import commands
import os

TOKEN = os.environ.get('DC_TOKEN')

bot = discord.Bot()

@bot.event
async def on_ready():
    print("Ready to go!")


bot.run(TOKEN)

