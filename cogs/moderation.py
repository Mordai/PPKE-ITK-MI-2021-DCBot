import discord
from discord.ext import commands
from discord import Option
from discord.app import SlashCommand
from dotenv import load_dotenv
import os

# Custom classes
from helpers.channel_ids import ChannelIDs

# Load/run nessesary components/functions
load_dotenv()

class ModerationTools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[os.getenv("ITK_SERVER_ID")])
    async def hello(ctx, name: Option(str, "Enter your name"), gender: Option(str, "Choose your gender", choices=["Male", "Female", "Other"]), age: Option(int, "Enter your age", required=False, default=18)):
        if ctx.channel.id == ChannelIDs.InformationChannels.csoport_assign:
            print("Okés, mehetünk tovább!")
        else:
            print("Nem jó csatorna!")
        await ctx.send(f"Hello {name}")

    def setup(bot):
        bot.add_cog(ModerationTools(bot))