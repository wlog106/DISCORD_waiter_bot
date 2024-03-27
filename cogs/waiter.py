import discord
from discord.ext import commands
import json
from cogs.__init__ import Init
from cogs.mod import cac_stor

with open("./cogs/menu.json" ,"r" ,encoding = "utf-8") as file:
    menu = json.load(file)

class Waiter(Init):

    @commands.Cog.listener()
    async def on_ready(self):
        print("bot is on ready")

    @commands.command()
    async def add(self,msg):
        message = str(msg.message.content)[5:]
        if message in menu["for_waiter"]:
            ename = cac_stor.ename(message)
            cac_stor.lunch(ename)
            await msg.channel.send("成功訂購" + message + "!")
               
    @commands.command()
    async def total(self,ctx):
        total = cac_stor.total()
        await ctx.send("總金額 : " + str(total))

    @commands.command()
    async def reset(self,ctx):
        cac_stor.init()
        await ctx.send("已重置")

    @commands.command()
    async def amount(self, ctx):
        message = str(ctx.message.content)[8:]
        if message in menu["for_waiter"]:
            ename = cac_stor.ename(message)
            price = cac_stor.price_i(ename)
            amount = cac_stor.amount(ename)
            await ctx.send(message + " : " + str(amount) + "個")
            await ctx.send("共 : " + str(price) + "元")

    @commands.command()
    async def list(self, ctx):
        await ctx.send("--------------")
        for i in range(0,9):
            ename = menu["items"][i]["ename"]
            amount = cac_stor.amount(ename)
            if amount == 0:
                continue
            price = cac_stor.price_i(ename)
            cname = menu["items"][i]["cname"]
            await ctx.send(cname + " : " + str(amount) + "個")
            await ctx.send("共 : " + str(price) + "元")
            await ctx.send("--------------")
    
    @commands.command()
    async def menu(self, ctx):
        for i in range(0,9):
            cname = menu["items"][i]["cname"]
            price = menu["items"][i]["price"]
            await ctx.send(cname + " : " + str(price) + "元")

    @commands.command()
    async def delete(self, msg):
        message = str(msg.message.content)[8:]
        if message in menu["for_waiter"]:
            ename = cac_stor.ename(message)
            amount = cac_stor.delete(ename)
            if amount == 0:
                await msg.send("商品數已為0")
            elif amount > 0:
                await msg.send("成功刪除" + message + "!")

async def setup(bot):
    await bot.add_cog(Waiter(bot))