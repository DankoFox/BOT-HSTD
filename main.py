#khai báo
import discord
import random
import os
# -*- coding: utf-8 -*-

#import vài thứ
from keep_alive import keep_alive

from discord.ext import commands
intents = discord.Intents.all()

from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix='.', intents=intents)

def randome(index):
	s = ' '
	for x in range(0, index):
		s += str(random.randint(0, 9))
	return s
  
##GARDEN OF WORD################################
from garden_of_words import NON, sad, chao, chaolai, LUUY, DAPENIS, EBALL, khaled_quotes
##GARDEN OF WORD################################

##ScrapeWeb#####################################
from WebScraping import tudien, idiom
##ScrapeWeb#####################################

##APIs##########################################
from TheAPIs import dark, pune, weatha, synon, daoly, fact, kaynewest, encourage
##APIs##########################################

##ALPHABET########################################
from alphabet import chucai  ##Thank you Danh##
##ALPHABET########################################

#CODE CHÍNH____________________________________________________________________________

@client.event
async def on_ready():
	print('{0.user} JOINED ! '.format(client))

@client.event
async def on_member_join(member):
	print(f'{member} in ')

@client.event
async def on_member_remove(member):
	print(f'{member} out')

@client.event
async def on_message(message):
	msg = message.content
	if message.author == client.user:
		return

	if msg.startswith('.ciao'):
		await message.channel.send('Đạt chào bạn nhá')

	if msg.startswith('.penis'):
		await message.channel.send(DAPENIS)

	if any(word in msg.lower() for word in chao):
		await message.channel.send(random.choice(chaolai))

	if any(word in msg.lower() for word in sad):
		context = encourage()
		await message.channel.send(context)

	if msg.startswith('.fact'):
		useless = fact()
		await message.channel.send(useless)

	await client.process_commands(message)


#Chuyển sang dùng command__________________________________________________

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong ! {round(client.latency*1000)} ms')

@client.command()
async def bruh(ctx):
	lmao = '**theBRUH**'
	await ctx.send(f'||{lmao}||')

@client.command()
async def dak(ctx):
	dajoke = dark()
	await ctx.send(dajoke)

@client.command()
async def pun(ctx):
	dajoke = pune()
	await ctx.send(dajoke)

@client.command()
async def kayne(ctx):
	Niggainfrance = kaynewest()
	await ctx.send(Niggainfrance + ' - Kayne West')

@client.command()
async def ran(ctx, a: int):
	ngaunhien = randome(a)
	await ctx.send(ngaunhien)

@client.command()
async def dic(ctx,*,a):
	try:
		embed = discord.Embed(colour=discord.Colour.orange())
		tungu = tudien(a.lower())
		embed.set_footer(text=tungu)
		await ctx.send(embed=embed)
	except:
		await ctx.send('Đạt éo biết từ này')

@client.command()
async def ball(ctx):
	embed = discord.Embed(colour=discord.Colour.blue())
	embed.set_footer(text=random.choice(EBALL))
	await ctx.send(embed=embed)

@client.command()
async def non(ctx):
	await ctx.send(NON)

@client.command()
async def syno(ctx, *, a):
	output = synon(a)
	await ctx.send(f"```{output}```")

@client.command()
async def weather(ctx):
	weather = weatha()
	await ctx.send(weather)

@client.command()
async def texty(ctx, *, a):
	output_chu_cai = chucai(a)
	await ctx.send(output_chu_cai)

@client.command()
async def idm(ctx):
	thanhngu = idiom()
	await ctx.send(f"```{thanhngu}```")

##yesh

@client.command()
async def acquy(ctx):
	await ctx.send(file=discord.File('acquy.jpg'))

@client.command()
async def daoli(ctx):
  quote = daoly()
  await ctx.send(f"> {quote}")

@client.command()
async def khaled(ctx):
  quote = random.choice(khaled_quotes)
  await ctx.send(f"> {quote} - DJ Khaled")

keep_alive()
TOKEN = os.getenv('TOKEN')

try:
  client.run(TOKEN)
except:
  print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
