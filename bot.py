import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='*')

@bot.event 
async def on_ready():
 print(">>GARY Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(867404616371273729)
    await channel.send(F'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(867404711556677632)
    await channel.send(F'{member} leave!')

bot.run('ODY3NTAwNzUxOTI4NTU3NTk4.YPiBCA.yP7k_PrXiLS66Av7YelwudWNZsg')