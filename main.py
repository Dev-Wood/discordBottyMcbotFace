import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
import discord, datetime, time
from discord.ext import commands
from discord.ext.commands import Bot
from keep_alive import keep_alive
from datetime import datetime
from pytz import timezone
import random
import praw

reddit = praw.Reddit(client_id = "7OkB8binDPnOJw", client_secret = "	rmkm8QnkFpIcft2oEYHbDszzQIKZLw", username = "BurnerPraw123", password = "BurnerPraw123", user_agent = "pyBot")
#dont use this!

keep_alive()
counter = 0
intents = discord.Intents(members=True)
bot = commands.Bot(command_prefix="!")
client=discord.Client(intents=intents)
number = random.randint(0,1)




@bot.command(help='To see if im working')
async def ping(ctx):
	await ctx.channel.send("pong")

@bot.command(help='Cool guys')
async def credits(ctx):
	await ctx.channel.send("I was created by Ian and Manhar")

@bot.command(help='Wassup')
async def hello(ctx):
	await ctx.channel.send("Hello👋")


@bot.command(help='Whatever today is')
async def today(ctx):
  now_time = datetime.now(timezone('US/Eastern'))
  fmt = "%b %d, %Y %H:%M"
  day = now_time.strftime(fmt)
  await ctx.channel.send(day)

@bot.command(help='It is a nice haircut')
async def nicecut(ctx):
  embed=discord.Embed(title="Nice Cut G", url="https://youtu.be/JFGJQLCarqk")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/spongefan/images/1/1a/Ilikeyacutg.jpg/revision/latest?cb=20201215162733")
  embed.add_field(name="Nice", value="Cut G", inline=False)
  await ctx.send(embed=embed)

@bot.command(help='Why not')
async def why(ctx):
	await ctx.channel.send('We Were Bored')

@bot.command(help='Adding command')
async def countAdd(ctx):
	global counter
	counter += 1
	await ctx.channel.send(counter)

@bot.command(help='Only works for CountMod role')
@commands.has_role('CountMod')
async def countReset(ctx):
	global counter
	counter = 0
	await ctx.channel.send('The counter has been reset and is now 0')

@bot.command(help='Flips a coin')
async def coinflip(ctx):
	number = random.randint(0,1)
	if(number == 1):
		await ctx.channel.send('**Heads**')
	else:
		await ctx.channel.send('**Tails**')
 
@bot.command(name='pingme', help=' Pings the author of the message')
async def pingme(ctx):
	await ctx.send(ctx.author.mention)

@bot.command(help=' Rolls a 20 sided die')
async def d20(ctx):
	ResA = random.randint(1,20)
	await ctx.channel.send('**your role on a 20 sided die was**')
	await ctx.channel.send(ResA)

@bot.command(help='Definitely No')
async def no(ctx):
	await ctx.channel.send('yes')

@bot.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

bot.run("token")
