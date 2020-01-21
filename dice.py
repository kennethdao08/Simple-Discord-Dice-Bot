import discord
from random import randint
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print("Bot is online.")

@bot.command()
async def roll(ctx, num_of_rolls: int, sides: int):
    #await ctx.send(f")
    rolled = [randint(1, sides) for _ in range(num_of_rolls)]
    total = sum(rolled)
    await ctx.send(f"Rolling {num_of_rolls}d{sides}...\nYou rolled: {str(rolled)[1:-1]}\nTotal: {total}")


# Bot token currently inactive
bot.run("NjMzNDYzNzYzNTcxMzEwNjAz.XaUVKA.X18n4S_lIDET3TGdoX86KzPxQO8")
