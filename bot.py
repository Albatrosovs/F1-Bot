import discord
from discord.ext import commands
from config import settings as set
from config import urls

def run_bot():
    intents = discord.Intents.default() # бот имеет полные права доступа
    intents.message_content = True
    bot = commands.Bot(command_prefix = set['prefix'], intents = intents)

    @bot.command()
    async def mamamia(ctx):
        embed = discord.Embed(color = 0xff2800)
        embed.set_image(url = urls['mamamia'])
        await ctx.send(embed = embed)

    # @bot.command()
    # async def bolid(ctx):
    #     embed = discord.Embed(color = 0xff2800)
    #     embed.set_image(url = urls['bolid'])
    #     await ctx.send(embed = embed)

    @bot.command()
    async def bolid(ctx):
        await new_command(ctx,0xff2800,'bolid')

    async def new_command(ctx,color,url):
        embed = discord.Embed(color = color)
        embed.set_image(url = urls[url])
        await ctx.send(embed = embed)
    
    bot.run(set['token'])