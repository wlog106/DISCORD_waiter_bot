import discord
from discord.ext import commands
import asyncio
import os
import json

with open("setting.json","r",encoding = "utf-8") as file:
    setting = json.load(file)

bot = commands.Bot(command_prefix=".",intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("\nlaunch successfully\n")

@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"loaded {extension} done.")

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"unloaded {extension} done.")

@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"reloaded {extension} done.")    

async def Load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
           await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await Load()
        await bot.start(setting["TOKEN"])
        
if __name__=="__main__":
    asyncio.run(main())