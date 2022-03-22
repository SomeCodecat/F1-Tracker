import os
from discord import Client, Intents, Embed
import json
from discord.ext import tasks
from dotenv import load_dotenv
from load import jsonRequest
from api import api_call
from discord_slash import SlashCommand, SlashContext

# Get a stat from the "current_results.json" file in this case the "season"
# f = open("current_results.json")
#    stats = json.load(f)
#
#    print(stats["MRData"]["RaceTable"]["season"])

# load in the environment variables (.env)
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

prefix = "!"
bot = Client(intents=Intents.default())
slash = SlashCommand(bot, sync_commands=True)


@ slash.slash(name="test")
async def test(ctx: SlashContext):
    embed = Embed(title="Embed Test")
    await ctx.send(embed=embed)


@ bot.event
async def on_ready():
    print(f"{bot.user} is Online!")


@ tasks.loop(seconds=60)
async def api_request():
    api_call()


@ bot.event
async def on_message(message):
    if message.content == prefix + "f1":
        f = open("current_results.json")
        stats = json.load(f)

        season = stats["MRData"]["RaceTable"]["season"]
        round = stats["MRData"]["RaceTable"]["Races"][0]["round"]
        length_results = len(
            stats["MRData"]["RaceTable"]["Races"][0]["Results"])
        for i in range(0, length_results):
            print(stats["MRData"]["RaceTable"]["Races"]
                  [0]["Results"][i]["Driver"]["driverId"])

        await message.channel.send("Season: " + season + "\nRound: " + round)

api_request.start()
bot.run(TOKEN)
