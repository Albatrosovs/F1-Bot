import discord
from discord.ext import commands
from config import settings as set
from config import urls
from config import colors

def run_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix = set['prefix'], intents = intents)

    @bot.command()
    async def mamamia(ctx):
        await new_command(ctx,'ferrari','mamamia')

    @bot.command()
    async def bolid(ctx):
        await new_command(ctx,'ferrari','bolid')

    @bot.command()
    async def horner(ctx):
        await new_command(ctx,'redbull','horner')

    @bot.command()
    async def auf(ctx):
        await new_command(ctx,'mercedes','auf')

    @bot.command()
    async def lechair(ctx):
        await new_command(ctx,'ferrari','lechair')

    @bot.command()
    async def leave(ctx):
        await new_command(ctx,'mercedes','leave')

    @bot.command()
    async def mazepin(ctx):
        await new_command(ctx,'haas','mazepin')

    @bot.command()
    async def classic(ctx):
        await new_command(ctx,'ferrari','classic_ferrari')

    @bot.command()
    async def kind_gasly(ctx):
        await new_command(ctx,'alpine','kind_gasly')

    @bot.command()
    async def piston(ctx):
        await new_command(ctx,'ferrari','piston')

    @bot.command()
    async def genshin(ctx):
        await new_command(ctx,'f1','genshin')

    @bot.command()
    async def max(ctx):
        await new_command(ctx,'mercedes','max')

    @bot.command()
    async def goatifi(ctx):
        await new_command(ctx,'williams','goatifi')

    @bot.command()
    async def beer(ctx):
        await new_command(ctx,'alfaromeo','beer')

    @bot.command()
    async def clowns(ctx):
        await new_command(ctx,'ferrari','clowns')

    @bot.command()
    async def strategy(ctx):
        await new_command(ctx,'ferrari','strategy')

    async def new_command(ctx,color,url):
        embed = discord.Embed(color = colors[color])
        embed.set_image(url = urls[url])
        await ctx.send(embed = embed)
    
    bot.run(set['token'])