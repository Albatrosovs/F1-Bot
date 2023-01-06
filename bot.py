import discord
import random
from discord.ext import commands
import config
import requests
import json

def run_bot():
    intents = discord.Intents.default() # бот имеет полные права доступа
    intents.message_content = True
    bot = commands.Bot(command_prefix = config.prefix, intents = intents)

    @bot.command()
    async def rand(ctx, *arg):
        await ctx.reply(random.randint(0,100))

    @bot.command()
    async def hello(ctx):
        author = ctx.message.author
        await ctx.send(f'Hello, {author.mention}!')

    @bot.command()
    async def fox(ctx):
        response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
        print(response.text)
        json_data = json.loads(response.text) # Извлекаем JSON
        # print(json_data)

        embed = discord.Embed(color = 0xff9900, title = 'Random Fox') # Создание Embed'a
        embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
        await ctx.send(embed = embed) # Отправляем Embed
    
    bot.run(config.token)