import os
import discord
from discord.ext import commands, tasks
from web_server import keep_alive
from web_scraper import *
from url_website import *

token = os.environ["token"]

bot = commands.Bot(command_prefix = "$")

cost_change = None

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def new(ctx, url):
  if url[:8] == "https://":
    update_url(url)
    await ctx.send("Done")
  else:
    await ctx.send("Please input an acutal URL")

@bot.command()
async def website(ctx):
  await ctx.send(read_website())

@bot.command()
async def view(ctx):
  await ctx.send(return_price())

@tasks.loop(minutes = 1)
async def check():
  cost_change = price_change()

@bot.command()
async def start(ctx):
  check.start()
  await ctx.send("Successfully activated price monitor")
  print("started")

  if cost_change != None:
    await ctx.send("Note: Price dropped from " + cost_change[0] + " to " + cost_change[1])
    check.cancel()
    await ctx.send("Deactivated price monitor")
    print("ended")
    

@bot.command()
async def end(ctx):
  check.cancel()
  await ctx.send("Successfully deactivated price monitor")
  print("ended")

keep_alive()
bot.run(token)