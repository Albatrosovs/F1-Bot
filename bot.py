import discord
import random
from discord.ext import commands

def run_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.command()
    async def rand(ctx, *arg):
     await ctx.reply(random.randint(0,100))
    
    bot.run('MTA2MDY0Mzc0MzMzNTcxNDg3Ng.GGTpdi.Sq8YzJ7kMjWqxMcoZrCYqEFakZ0917tgpMAQac')