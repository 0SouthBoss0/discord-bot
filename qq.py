import discord
import random
import aiohttp
import io
from discord.ext import commands
import dictionary

TOKEN = 'NzU0Mzk0Mjk2NDA4NjA0NzE0.X10GcA.UVm33-R0RJKY80R4Mktu0SrPbLg'
bot = commands.Bot(command_prefix='-')


@bot.event
async def on_ready():
    print("JK BOT IS ON! HAVE FUN!")


@bot.command()
async def helpme(ctx):
    await ctx.send("-rep для повторения фразы; -play для игры в рулетку")


# to turn on other commands delete on_message
@bot.event
async def on_message(message):
    args = message.content.split(" ")[1:]
    for i in range(len(dictionary.a)):
        if dictionary.a[i] in message.content.lower():
            await message.delete()


@bot.command()
async def rep(ctx, *args):
    response = ""
    for arg in args:
        response = response + " " + arg

    await ctx.channel.send(response)


@bot.command()
async def play(ctx, args):
    q = random.randint(0, 5)
    if args == str(q):
        await ctx.send("Попал")
    else:
        await ctx.send("Косой")


@bot.command()
async def upload(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.pcgamesn.com/wp-content/uploads/2020/10/lord-tachanka.jpg")   as resp:
            if resp.status != 200:
                return await ctx.channel.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await ctx.channel.send(file=discord.File(data, 'cool_image.png'))


async def kick(ctx, member: discord.member, *, reason="Паскаль"):
    await member.kick(reason=reason)


bot.run(TOKEN)
