from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord.ext import commands
import discord, requests, os

channel_id = 959440578121187429
bot = commands.Bot(command_prefix="dog ")

@bot.command(name="pic")
async def Dog(ctx):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    image_link = response.json()["message"]
    await ctx.send(image_link)

async def lyssas_legions():
    await bot.wait_until_ready()
    c = bot.get_channel(channel_id)
    await c.send("Lyssa's Legions opens in 30 minutes! Gather players!")

async def melandrus_matchup():
    await bot.wait_until_ready()
    c = bot.get_channel(channel_id)
    await c.send("Melandru's Matchup opens in 30 minutes! Gather players!")

async def grenths_game():
    await bot.wait_until_ready()
    c = bot.get_channel(channel_id)
    await c.send("Grenth's Game opens in 30 minutes! Gather players!")

@bot.event
async def on_ready():
    print("Ready")

    scheduler = AsyncIOScheduler()

    scheduler.add_job(lyssas_legions, CronTrigger(hour="20", minute="30", second="0")) 
    scheduler.add_job(melandrus_matchup, CronTrigger(hour="23", minute="30", second="0")) 
    scheduler.add_job(grenths_game, CronTrigger(hour="17", minute="30", second="0")) 

    scheduler.start()

if __name__ == '__main__':
    bot.run(os.environ["TOKEN"])